using System;
using System.ComponentModel;
using System.Linq;
using System.Web.Services;

namespace StandardSoapServer
{
	[WebService(Namespace = "http://db.com/")]
	[WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
	[ToolboxItem(false)]
	public class CalculatorService : WebService
	{
		[WebMethod]
		public int Add(int x, int y)
		{
			return x + y;
		}

		[WebMethod]
		public int Subtract(int x, int y)
		{
			return x - y;
		}
	}
}