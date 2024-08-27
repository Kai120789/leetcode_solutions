class Solution:
    def isValid(self, s: str) -> bool:
        mas = list(s)
        if (len(s) % 2 == 1):
            return False
        else:
            count = 0
            while count < len(mas)-1:
                
                if (mas[count] == '(' and mas[count+1] == ')'):
                    mas.pop(count+1)
                    mas.pop(count)
                    count = 0
                    
                elif (mas[count] == '[' and mas[count+1] == ']'):
                    mas.pop(count+1)
                    mas.pop(count)
                    count = 0
                
                elif (mas[count] == '{' and mas[count+1] == '}'):
                    mas.pop(count+1)
                    mas.pop(count)
                    count = 0

                else:
                    count += 1
                
                


            while True:
                if(mas == []):
                    return True

                if(mas[0] == '('):
                    if(')' in mas and (mas.index(')') % 2 == 1)):
                        mas.pop(mas.index(mas[0]))
                        mas.pop(mas.index(')'))
                        print(mas)
                    else:
                        return False

                elif(mas[0] == '['):
                    if(']' in mas and (mas.index(']') % 2 == 1)):
                        mas.pop(mas.index(mas[0]))
                        mas.pop(mas.index(']'))
                        print(mas)
                    else:
                        return False

                    
                
                elif(mas[0] == '{'):
                    if('}' in mas and (mas.index('}') % 2 == 1)):
                        mas.pop(mas.index(mas[0]))
                        mas.pop(mas.index('}'))
                        print(mas)
                    else:
                        return False
                else:
                    return False
            
            

                    
            