import os
import time
# Run the first command


while True:
    # Run the command
    status = os.system("scrapy crawl fptshop")

    # Check the exit status
    if status == 0:
        # The command succeeded, so break out of the loop
        break
    else:
        # The command failed, so wait for a bit and try again
        time.sleep(10)


# Run the second command
# while True:
#     # Run the command
#     status = os.system("scrapy crawl tgdd")

#     # Check the exit status
#     if status == 0:
#         # The command succeeded, so break out of the loop
#         break
#     else:
#         # The command failed, so wait for a bit and try again
#         time.sleep(10)


# while True:
#     # Run the command
#     status = os.system("scrapy crawl dienmayxanh")


#     # Check the exit status
#     if status == 0:
#         # The command succeeded, so break out of the loop
#         break
#     else:
#         # The command failed, so wait for a bit and try again
#         time.sleep(10)

# while True:
#     # Run the command
#     status = os.system("scrapy crawl hoanghamobile")

#     # Check the exit status
#     if status == 0:
#         # The command succeeded, so break out of the loop
#         break
#     else:
#         # The command failed, so wait for a bit and try again
#         time.sleep(10)

