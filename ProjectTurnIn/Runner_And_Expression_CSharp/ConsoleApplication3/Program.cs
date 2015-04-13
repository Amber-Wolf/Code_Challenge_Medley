using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication3
{
    class Program
    {
        Random rand;

        const int PLUS = 0;
        const int MINUS = 1;
        const int TIMES = 2;
        const int DEVIDE = 3;

        static void Main(string[] args)
        {
            new Program();
        }

        Program()
        {
            rand = new Random();
            bool exit = false;
            int value;
            string result = "";
            while (!exit)
            {
                value = makeExpression(3,out result);
                Console.WriteLine("Expression is: " + result);
                Console.WriteLine("Value is: " + value);
                Console.WriteLine("Write 0 to exit, continue otherwise.");
                exit = 0 == Convert.ToInt32(Console.ReadLine());
            }
            exit = false;
            Runner run = new Runner();
            while (!exit)
            {
                int inBegin, inEnd, outBegin, outEnd;
                Console.WriteLine("Enter begin time in seconds for interval:");
                inBegin = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("Enter end time in seconds for interval:");
                inEnd = Convert.ToInt32(Console.ReadLine());
                run.findTime(inBegin, inEnd, out outBegin, out outEnd);
                Console.WriteLine("Longest time on that interval: " + outBegin + ", " + outEnd);
                Console.WriteLine("Write 0 to exit, continue otherwise.");
                exit = 0 == Convert.ToInt32(Console.ReadLine());
            }
        }

        int makeExpression(int depth, out string expr)
        {
            if (depth <= 0)
            {
                int value = rand.Next(19);
                value -= 9;
                expr = "" + value;
                return value;
            }
            int expressionType = rand.Next(3);
            string rightSide;
            string leftSide;
            int val1, val2;
            switch(expressionType){
                case PLUS:
                    val1 = makeExpression(depth - 1, out leftSide);
                    val2 = makeExpression(depth - 1, out rightSide);
                    expr = "( " + leftSide + " + " + rightSide + " )";
                    return val1 + val2;
                case MINUS:
                    val1 = makeExpression(depth - 1, out leftSide);
                    val2 = makeExpression(depth - 1, out rightSide);
                    expr = "( " + leftSide + " - " + rightSide + " )";
                    return val1 - val2;
                case TIMES:
                    val1 = makeExpression(depth - 1, out leftSide);
                    val2 = makeExpression(depth - 1, out rightSide);
                    expr = "( " + leftSide + " * " + rightSide + " )";
                    return val1 * val2;
                case DEVIDE:
                    val1 = makeExpression(depth - 1, out leftSide);
                    val2 = makeExpression(depth - 1, out rightSide);
                    expr = "( " + leftSide + " / " + rightSide + " )";
                    return val1 / val2;
            }
            expr = "";
            return 0;
        }
    }
}
