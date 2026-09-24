while True:
    i = input()
    if i =="0":
        break
    else:
        h,w,icon,heart=i.split()
        h,w,heart=map(int,(h,w,heart))
        if heart == 1:
            for _ in range(h):
                print(icon*w)
        else:
            print(icon*w)
            for _ in range(h-2):
                print(icon+" "*(w-2)+icon)
            print(icon*w)
