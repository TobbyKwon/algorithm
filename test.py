# -*- coding: utf-8 -*-
import Palindrome

str1 = input("회문 판별할 문장을 입력하세요. : ")

result = Palindrome.ispalindrome(str1)

if result == True:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")

