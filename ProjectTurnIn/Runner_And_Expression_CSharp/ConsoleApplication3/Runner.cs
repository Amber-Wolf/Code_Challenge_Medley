using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication3
{
    class Runner
    {
        char[] delimiterChars = { ' ', '\t', '-', '\f', '\v', '\r', '\n' };
        Split[] splits;

        public Runner()
        {
            readFileIn("run.txt");

        }

        void readFileIn(string source)
        {
            string text = System.IO.File.ReadAllText(source);
            string[] words = text.Split(delimiterChars);
            splits = new Split[words.Length / 5];
            for (int x = 0; x < splits.Length; x++)
            {
                int t = Convert.ToInt32(words[x * 5]);
                int hR = Convert.ToInt32(words[x * 5 + 1]);
                string[] temp = words[x * 5 + 2].Split(':');
                int mP = Convert.ToInt32(temp[0]);
                int sP = Convert.ToInt32(temp[1]);
                int c = Convert.ToInt32(words[x * 5 + 3]);
                splits[x] = new Split(t,hR,mP,sP,c);
            }
        }

        int findTimeHelper(int timeLow, int timeHigh, int index)
        {
            while ((index < splits.Length) && (timeLow <= splits[index].getPace()) && (timeHigh >= splits[index].getPace()))
            {
                index++;
            }
            return index;
        }

        public void findTime(int timeLow, int timeHigh, out int bestBeginTime, out int bestEndTime)
        {
            bestBeginTime = 0;
            bestEndTime = 0;
            int tempBegin, tempEnd;
            for (int x = 0; x < splits.Length; x++)
            {
                int pace = splits[x].getPace();
                if ((pace >= timeLow) && (pace <= timeHigh))
                {
                    tempBegin = x;
                    tempEnd = findTimeHelper(timeLow,timeHigh,x);
                    x = tempEnd;
                    if ((splits[tempEnd].getTime() - splits[tempBegin].getTime()) >= (bestEndTime - bestBeginTime))
                    {
                        bestBeginTime = splits[tempBegin].getTime();
                        bestEndTime = splits[tempEnd].getTime();
                    }
                }
            }
        }

        class Split
        {
            int time;
            int heartRate;
            int paceTime;
            int cadence;

            public Split()
            {

            }

            public Split(int t, int hR, int mP, int sP, int c) 
            {
                time = t;
                heartRate = hR;
                paceTime = mP * 60 + sP;
                cadence = c;
            }

            public int getPace()
            {
                return paceTime;
            }

            public int getTime()
            {
                return time;
            }
        }
    }


}
