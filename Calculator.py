class calculator:
    def __init__(self):
        self.result = 0;
    def getValue(self):
        return self.result;
    def setValue(self, v):
        self.result = v;

    def plus(self, num1, num2):
        self.result = num1 + num2;
        return self.result;
    def minus(self, num1, num2):
        self.result = num1 - num2;
        return self.result;
    def mul(self, num1, num2):
        self.result = num1 * num2;
        return self.result;
    def dev(self, num1, num2):
        self.result = num1 / num2;
        return self.result;

if __name__ == '__main__':
    mycal = calculator();
    num1 = int(input("숫자1:"));
    num2 = int(input("숫자2:"));
    sym = input("기호(+, -, *, /):");

    if sym == "+":
        result = mycal.plus(num1, num2);
        print(result);
        mycal.setValue(result);
    elif sym == "-":
        result = mycal.minus(num1, num2);
        print(result);
        mycal.setValue(result);
    elif sym == "*":
        result = mycal.mul(num1, num2);
        print(result);
        mycal.setValue(result);
    elif sym == "/":
        result = mycal.dev(num1, num2);
        print(result);
        mycal.setValue(result);

    print("결과:", mycal.getValue());







