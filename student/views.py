from django.shortcuts import HttpResponse, render 
import json
from django.http import JsonResponse

def read_create(request) :
    try :
        f = open("student\students.json")
        data = json.load(f)
        f.close()
        if request.method == "GET" : 
            return JsonResponse(data , safe=False)
        elif request.method == "POST" : 
            data.append(json.loads(request.body))
            with open("student\students.json", "w") as outfile:
                json.dump(data, outfile)
            return JsonResponse({"status" : "Added successfully"})
    except Exception as e:
        return JsonResponse({"status" : str(e)})

def update_delete(request , id) :
    try :
        founded = False 
        f = open("student\students.json")
        data = json.load(f)
        f.close() 
        for i in range(0 , len(data)) : 
            print(data[i])
            if data[i]["id"] == id : 
                founded = True 
                if request.method == "PUT" : 
                    data[i] = json.loads(request.body)
                    with open("student\students.json", "w") as outfile:
                        json.dump(data, outfile)
                    return JsonResponse({"status" : "Updated successfully"})
                elif request.method == "DELETE" : 
                    del data[i]
                    with open("student\students.json", "w") as outfile:
                        json.dump(data, outfile)
                    return JsonResponse({"status" : "Deleted successfully"})
                else : 
                    return JsonResponse({"status" : "bad request method"})

                break 
        if not founded : 
             return JsonResponse({"status" : "Not found"})
    except Exception as e:
        return JsonResponse({"Message" : str(e)}) 


