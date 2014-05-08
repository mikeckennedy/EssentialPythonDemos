using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace client2
{
    class Program
    {
        static void Main(string[] args)
        {
            var c = new localhost.CalculatorService();
            var s = c.Add(1, 2);
            Console.WriteLine(s);
        }
    }
}
