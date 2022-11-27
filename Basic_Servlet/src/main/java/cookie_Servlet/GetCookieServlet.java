package cookie_Servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class GetCookieServlet
 */
@WebServlet("/GetCookieServlet")
public class GetCookieServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public GetCookieServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
//		response.getWriter().append("Served at: ").append(request.getContextPath());
//		
		
		PrintWriter out = response.getWriter();
		response.setContentType("text/html");
		
		Cookie[] ck = request.getCookies();
		
		String bg_Color = "#FFFFFF";
		String text_Color = "#000000";
		String font_Weight = "normal";
		String font_Style = "normal";
		String text_Size = "90px";
		
		if(ck!=null)
		{
			if(ck.length >0 && ck[0].getValue() != null)
			{
				bg_Color = ck[0].getValue();
			}
			
			if(ck.length> 1 && ck[1].getValue() != null)
			{
				text_Color = ck[1].getValue();
			}
			
			if(ck.length > 2 && ck[2].getValue() != null)
			{
				if(ck[2].getValue().equals("true"))
				{
					font_Weight = "bold";
				}
			}
			
			if(ck.length > 3 && ck[3].getValue() != null)
			{
				if(ck[3].getValue().equals("true"))
				{
					font_Style = "italic";
				}
			}
			
			if(ck.length > 4 && ck[4].getValue() !=null)
			{
//				if(ck[4].getValue().equals("true"))
//				{
					text_Size = "90px";
//				}
			}
			
		}
		
		out.println("<label style='background-color:"+bg_Color+";color:"+text_Color+";font-weight:"
				+font_Weight+";font-style:"+font_Style+";font-size:"+text_Size+"'>Hello World!!</label>");
		
		
//		PrintWriter out = response.getWriter();
//		response.setContentType("text/html");
//		
//		Cookie[] ck = request.getCookies();
//		
//		String bg_color = "#FFFFFF";
//		String text_color = "#000000";
//		String font_weight = "normal";
//		String font_style = "normal";
//		
//		if(ck!=null) {
//			if(ck.length > 0 && ck[0].getValue()!=null) {
//				bg_color = ck[0].getValue();
//			}
//			if(ck.length > 1 && ck[1].getValue()!=null) {
//				text_color = ck[1].getValue();
//			}
//			if(ck.length > 2 && ck[2].getValue()!=null) {
//				if(ck[2].getValue().equals("true")) {
//					font_weight = "bold";
//				}
//			}
//			if(ck.length > 3 && ck[3].getValue()!=null) {
//				if(ck[3].getValue().equals("true")) {
//					font_style = "italic";
//				}
//			}
//			
//			if(ck.length > 4 && ck[4].getValue()!=null) {
//				if(ck[4].getValue().equals("true")) {
//					font_weight = "underline";
//				}
//			}
//		}
//		
//		
//		
//		out.println("<label style='background-color:"+bg_color+";color:"+text_color+";font-weight:"+font_weight+";font-style:"+font_style+";'>Hello World!!</label>");	
//	
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
