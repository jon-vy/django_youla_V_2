PhoneNum = '+7 (921) 561-45-15'
phone = PhoneNum.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
print(phone)







# import asyncio
# from asyncio import Semaphore
#
#
# async def link_count(semaphore):
#     await semaphore.acquire()
#     # какой то код
#     semaphore.release()
#
# async def gahter():
#     semaphore = Semaphore(20)
#     tasks = []
#     for link_count, link in enumerate(links_item):
#         link_item = f"https://{link.strip()}"
#         task = asyncio.create_task(link_count(semaphore))
#         tasks.append(task)
#     await asyncio.gather(*tasks)

