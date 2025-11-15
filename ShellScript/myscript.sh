#!/bin/bash
# special variables
echo "Script Name: $0"       # name of the file
echo "First arg  : $1"       # after file neme, first arguments
echo "Second Arg : $2"       # second arguments
echo "All args   : $@"       # list of given arguments
echo "Total args : $#"       # count total arguments

# bash --version           # showing bash version

# variable assigned, without space
#name="Sandeep"

#echo "Hello script! $name!"     # output shows

#todo: concatenate
# greeting="Hello, "
# name="World!"

# echo "$greeting$name"

#todo: Arithmetic
# num1=10
# num2=30
# echo $((num1 + num2))


#todo: Array
# fruits=("apple" "banana" "cherry" "date")   # each element separated by space not with comma(,)
# echo ${fruits[0]}   # apple
# echo ${fruits[1]}   # banana
# echo ${fruits[2]}   # kiwi 

# echo " "
# for loop
# for fruit in ${fruits[@]}; do
#   echo $fruit
# done


#todo: for loop
#  [@] it means all elements 
# for fruit in "${fruits[@]}"
# do
#   echo "I liked $fruit"
# done



#todo: if..else.fi  statement

# num=5

# if [ $num -gt 10 ]
# then
#   echo "Number is greater than 10"
# else
#   echo "Number is less than 10"
# fi  

#todo: elif statement

# num=0

# if [ $num -gt 0 ]
# then
#   echo "Number is positive"
# elif [ $num -lt 0 ]
# then
#   echo "Number is negative"
# else
#   echo "Number is zero"
# fi      

# echo " " 

# # next example
# num=-0
# if [ $num -gt 10 ]; then
#   echo "Number is greater thatn 10"
# elif [ $num -lt 10 ]; then
#   echo "Number is less than 10"
# elif [ $num -eq 10 ]; then
#   echo "Number is equal to 10"
# elif [ $num -lt 0 ]; then
#   echo "Negative number entered"
# else 
#   echo "Number is less than 10"
# fi  




#todo: for loops
# Example 1
# for i in {1..5}
# do
#   echo "Iteration $i"
# done  

# echo ""

# example two

# fruits=("apple" "banana" "mango")

# for fruit in "${fruits[@]}"
# do
#     echo "$fruit"
# done

# echo ""

# while loop

# count=1

# while [ $count -le 5 ]
# do
#   echo "count: $$count"
#   ((count++))
# done  

# runs forever
# while true 
# do 
#   echo "Forever runs"
# done  

# while read line
# do
#   echo "$line"
# done < myfile.txt

# example one
# my_function() {
#   echo "Hello function"
# }

# my_function     # calling a function to print


# Exampl two
# greet() {
#   local name=$1
#   echo  "Hello, $name!"
# }
# greet "Sandeep"

# echo -n "enter name : "
# read name
# echo "My name is $name"


