import click
from typing import Any, Dict, Callable,Tuple,List

sizes:Dict[str,int] = {"big":9,"medium":6,"small":3,"collection":2}
sizes_keys:List[str] = list(sizes.keys())

@click.command()
@click.option('--amount', prompt='Amount of products',
              help='Total amount of products to pack into bins',
              required=True, type=click.IntRange(1, 100))
@click.option('--convert_medium', prompt='Medium container fix',
              help='Converts 1 small and 1 large container into 2 medium sized',
              required=False, type=click.BOOL,default=True)
@click.option('--convert_large', prompt='Large container fix',
              help='Converts 1 medium container into one large sized',
              required=False, type=click.BOOL,default=True)

def solve(amount:int,convert_medium:bool=True,convert_large:bool=True) -> Dict [str, int]:
    solution:Dict[str,int] = {"small":0,"medium":0,"big":0,"collection":0}
  
    quotient:int  = 0
    remainder:int = amount

    #for index,key in enumerate(sizes.keys()):
  
    #nt("SIZES_KEYS :: ",sizes_keys)
    for index in range(0,len(sizes_keys)-1):
      
      #print("Start quotient : ",quotient,"  remainder : ",remainder," size: ",sizes[sizes_keys[index]])

      quotient, remainder = divmod(remainder,sizes[sizes_keys[index]])
      
      #print("Divmod quotient : ",quotient,"  remainder : ",remainder," size: ",sizes[sizes_keys[index]])

      if sizes_keys[index]!="small":
        quotient += 1 if remainder>sizes[sizes_keys[index+1]] else 0
        remainder = 0 if remainder>sizes[sizes_keys[index+1]] else remainder
        #print("NOT SMALL ",sizes_keys[index+1],"  ",(remainder>sizes[sizes_keys[index+1]])," q:",quotient," r:",remainder )
      else:
        quotient += 1 if remainder else 0
        solution[sizes_keys[index]] = quotient
        break   
      
      #print("processing index: ",index," quotient:",quotient,"remainder: ",remainder," ",sizes_keys[index])

      
      solution[sizes_keys[index]] = quotient

    '''
    quotient, remainder = divmod(amount,sizes["big"])
    quotient += 1 if remainder>sizes['medium'] else 0
    remainder = 0 if remainder>sizes['medium'] else remainder
    solution["big"] = quotient
    
    quotient, remainder = divmod(remainder,sizes["medium"])
    quotient += 1 if remainder>sizes['small'] else 0
    remainder = 0 if remainder>sizes['small'] else remainder  
    solution["medium"] = quotient

    quotient, remainder = divmod(remainder,sizes["small"])
    quotient += 1 if remainder else 0
    solution["small"] = quotient
    '''

    total:int = sum(solution.values())
    
    print("total : ",total,"  ",solution.values())

    quotient, remainder = divmod(total,sizes['collection'])#divmod(total,sizes['collection'])
    quotient += 1 if remainder else 0

    print("total : ",total," quotient: ",quotient,"  remainder: ",remainder)

    solution["collection"] = quotient

    if convert_medium:
      #while (solution['small']>=1) and (solution['big']>=1):
      while (solution['small']==1) and (solution['big']==1):
        solution['small'] -= 1
        solution['big'] -= 1
        solution['medium'] += 2
    
    if convert_large:
      #while (solution['medium']>=1 and (solution['big']>=1)):
      while (solution['medium']==1 and (solution['big']==1)):
        solution["big"]+=1
        solution["medium"]-=1

    print(solution)
    return solution

if __name__ == '__main__':
  #solve() 
  for x in range(1,36):
    print(f"Amount = {x} : ",end = '', flush=True)
    solve.callback(x)
  