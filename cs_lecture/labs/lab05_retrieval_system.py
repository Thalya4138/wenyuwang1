"""第 37、51 章：事务、检索证据和有步数限制的动作循环。没有调用语言模型。"""
import re
import sqlite3


def tokens(text):
    return set(re.findall(r'[a-z]+', text.lower()))


def build_database():
    db = sqlite3.connect(':memory:')
    db.execute('CREATE TABLE documents(id INTEGER PRIMARY KEY, title TEXT, body TEXT)')
    with db:
        db.executemany('INSERT INTO documents VALUES (?,?,?)', [
            (1, 'Queue', 'A queue processes items in arrival order.'),
            (2, 'BFS', 'Breadth first search uses a queue for shortest paths in unweighted graphs.'),
            (3, 'Heap', 'A heap provides efficient access to a minimum priority item.')])
    try:
        with db:
            db.execute("INSERT INTO documents VALUES (4,'Partial','temporary')")
            raise RuntimeError('模拟中途故障')
    except RuntimeError:
        pass
    assert db.execute('SELECT COUNT(*) FROM documents').fetchone()[0] == 3
    return db


def retrieve(db, query):
    wanted = tokens(query)
    candidates = []
    for identifier, title, body in db.execute('SELECT id,title,body FROM documents'):
        score = len(wanted & tokens(title+' '+body))
        if score:
            candidates.append((score, identifier, title, body))
    return sorted(candidates, key=lambda row: (-row[0], row[1]))


def bounded_assistant(db, query, max_steps=3):
    """确定性教学控制器：检索→读取证据→返回。不是完整 RAG/LLM 智能体。"""
    state = {'query': query, 'candidates': None, 'evidence': None}
    trace = []
    for step in range(max_steps):
        if state['candidates'] is None:
            state['candidates'] = retrieve(db, query)
            trace.append('retrieve')
        elif not state['candidates']:
            return {'status':'no_evidence','trace':trace}
        elif state['evidence'] is None:
            _, identifier, title, body = state['candidates'][0]
            state['evidence'] = {'document_id':identifier,'title':title,'quote':body}
            trace.append('read')
        else:
            return {'status':'evidence_found','evidence':state['evidence'],'trace':trace}
    return {'status':'budget_exhausted','trace':trace}


def main():
    db = build_database()
    found = bounded_assistant(db, 'queue shortest path')
    assert found['evidence']['document_id'] == 2
    assert bounded_assistant(db, 'photosynthesis')['status'] == 'no_evidence'
    assert bounded_assistant(db, 'queue', max_steps=1)['status'] == 'budget_exhausted'
    print('检索证据：', found)
    print('事务回滚、无证据与预算上限检查通过。')
    db.close()


if __name__ == '__main__':
    main()
