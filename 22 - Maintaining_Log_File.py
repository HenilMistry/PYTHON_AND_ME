# here, in this python i will show you that how we can maintain log files...
"""
For sack of simplicity, assume that here we are maintaining the log for user operations which user has performed
by running any menu-driven program...
    ex. calculator application...

Here I will be making a calculator application, and I will be maintaining logs of it...
"""
# importing a required modules...
import datetime
import os


# making the functions needed...
def add(*args):  # addition operation...
    answer = 0
    for x in args:
        answer += x
    return answer


def sub(*args):  # subtraction operation...
    answer = args[0]
    for x in args[1:]:
        answer -= x
    return answer


def mul(*args):  # multiplication operation...
    answer = 1
    for x in args:
        answer *= x
    return answer


def div(*args):  # division operation...
    answer = args[0]
    for x in args[1:]:
        answer /= x
    return answer


def mod(*args):  # modulo operation...
    answer = args[0]
    for x in args[1:]:
        answer %= x
    return answer


def clear():  # clearing the screen
    for i in range(0, 100):
        print("\n")


if __name__ == "__main__":
    contents_of_directory = os.listdir()
    date = datetime.datetime.now()
    file_exist = False
    if contents_of_directory.count("H_CalApp_LOGS.txt") > 0:
        file_exist = True

    name_of_user = input("Enter your name : ")
    permission_to_record_session = input("Will you permit us to record this session and make a log record (y/n): ")
    file = 0

    if file_exist:
        file = open("H_CalApp_LOGS.txt", 'a+')
    else:
        file = open("H_CalApp_LOGS.txt", 'x+')

    file.write("\n\nThe USER_NAME : "+name_of_user)
    file.write("\nThe starting time of session : "+str(date))

    wantToRun = True
    if permission_to_record_session.lower().__contains__('y') or permission_to_record_session.__contains__('1'):
        file.write("\nIterating first time...")
    else:
        file.write("\nUser doesn't give permission to record this session!!")
        file.close()
    while wantToRun:
        print("""
        You can choose the operations which you want to perform, either
        by writing a operation or by entering your choice...
        0 -> exit
        1 -> addition
        2 -> subtraction
        3 -> multiplication
        4 -> division
        5 -> modulo
        """)
        operation = input("Enter your choice or operation name : ")
        if operation.__contains__("1") or operation.lower().__contains__("add"):
            if permission_to_record_session.lower().__contains__('y') or permission_to_record_session.__contains__('1'):
                file.write("\nUser has entered : " + str(operation) + " Now, performing addition operation...")
            print("Addition Operation : ")
            a = int(input("Enter a : "))
            b = int(input("Enter b : "))
            print("Answer of operation : ", add(a, b))

            wantToRun = input("Do you want to use perform another operation : ")
            if wantToRun.lower().__contains__('y'):
                wantToRun = True
            else:
                if permission_to_record_session.lower().__contains__('y') or permission_to_record_session.__contains__(
                        '1'):
                    file.write("\nUser Doesn't want to use application anymore...so, closing the app...")
                    file.close()
                wantToRun = False
        elif operation.__contains__('2') or operation.lower().__contains__("sub"):
            if permission_to_record_session.lower().__contains__('y') or permission_to_record_session.__contains__('1'):
                file.write("\nUser has entered : " + str(operation) + " Now, performing subtraction operation...")
            print("Subtraction Operation : ")
            a = int(input("Enter a : "))
            b = int(input("Enter b : "))
            print("Answer of operation : ", sub(a, b))

            wantToRun = input("Do you want to use perform another operation : ")
            if wantToRun.lower().__contains__('y'):
                wantToRun = True
            else:
                if permission_to_record_session.lower().__contains__('y') or permission_to_record_session.__contains__(
                        '1'):
                    file.write("\nUser Doesn't want to use application anymore...so, closing the app...")
                    file.close()
                wantToRun = False
        elif operation.__contains__('3') or operation.lower().__contains__("mul"):
            if permission_to_record_session.lower().__contains__('y') or permission_to_record_session.__contains__('1'):
                file.write("\nUser has entered : " + str(operation) + " Now, performing multiplication operation...")
            print("Multiplication Operation : ")
            a = int(input("Enter a : "))
            b = int(input("Enter b : "))
            print("Answer of operation : ", mul(a, b))

            wantToRun = input("Do you want to use perform another operation : ")
            if wantToRun.lower().__contains__('y'):
                wantToRun = True
            else:
                if permission_to_record_session.lower().__contains__('y') or permission_to_record_session.__contains__(
                        '1'):
                    file.write("\nUser Doesn't want to use application anymore...so, closing the app...")
                    file.close()
                wantToRun = False
        elif operation.__contains__('4') or operation.lower().__contains__("div"):
            if permission_to_record_session.lower().__contains__('y') or permission_to_record_session.__contains__('1'):
                file.write("\nUser has entered : " + str(operation) + " Now, performing division operation...")
            print("Division Operation : ")
            a = int(input("Enter a : "))
            b = int(input("Enter b : "))
            print("Answer of operation : ", div(a, b))

            wantToRun = input("Do you want to use perform another operation : ")
            if wantToRun.lower().__contains__('y'):
                wantToRun = True
            else:
                if permission_to_record_session.lower().__contains__('y') or permission_to_record_session.__contains__(
                        '1'):
                    file.write("\nUser Doesn't want to use application anymore...so, closing the app...")
                    file.close()
                wantToRun = False
        elif operation.__contains__('5') or operation.lower().__contains__("mod"):
            if permission_to_record_session.lower().__contains__('y') or permission_to_record_session.__contains__('1'):
                file.write("\nUser has entered : " + str(operation) + " Now, performing modulo operation...")
            print("Modulo Operation : ")
            a = int(input("Enter a : "))
            b = int(input("Enter b : "))
            print("Answer of operation : ", mod(a, b))

            wantToRun = input("Do you want to use perform another operation : ")
            if wantToRun.lower().__contains__('y'):
                wantToRun = True
            else:
                if permission_to_record_session.lower().__contains__('y') or permission_to_record_session.__contains__(
                        '1'):
                    file.write("\nUser Doesn't want to use application anymore...so, closing the app...")
                    file.close()
                wantToRun = False
        else:
            if permission_to_record_session.lower().__contains__('y') or permission_to_record_session.__contains__('1'):
                file.write("\nUser has entered " + str(operation) + " Now closing the app...")
                file.close()
            wantToRun = False
