

class GetList():
    pass
'''
        category_bucket = []
        res = []
        for i in range(1,25):
            tt=[x.code for x in tags.filter(category_id=i)]
            category_name = Category.objects.get(id=i).name
            for x in tt:
                print(x)
                b = Master.objects.filter(tags__contains=x)
                print(len(b))

                for bb in b:
                    print("bb : ",bb, bb.file_num)
                    if bb.file_num not in res: 
                        res.append(bb.file_num) 
            category_bucket.append([
                category_name, len(res)])
            res = []
'''
