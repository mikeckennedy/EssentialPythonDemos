using System;
using System.Linq;
using DotNetClient.Services;

namespace DotNetClient
{
	internal class Program
	{
		private static void Main(string[] args)
		{
			CalculatorServiceSoapClient client = new CalculatorServiceSoapClient();
			Console.WriteLine("The sum of 1 and 7 is " + client.Add(1, 7));
		}
	}
}