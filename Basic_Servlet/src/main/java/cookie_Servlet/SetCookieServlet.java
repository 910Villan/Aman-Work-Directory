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
 * Servlet implementation class SetCookieServlet
 */
@WebServlet("/SetCookieServlet")
public class SetCookieServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public SetCookieServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		
		PrintWriter out = response.getWriter();
		response.setContentType("text/html");
		
		String bg_color = request.getParameter("bg_color");
		String text_color = request.getParameter("text_color");
		
		String bold_Text = "false";
		if(request.getParameter("bold")!=null)
		{
			bold_Text = "true";
		}
		
		String italic_Text = "false";
		if(request.getParameter("italic")!= null)
		{
			italic_Text="true";
		}
		
		String textSize = "false";
		if(request.getParameter("size")!=null)
		{
			textSize = "true";
		}
		
//		String underline_Text = "false";
//		if(request.getParameter("underline")!= null)
//		{
//			underline_Text="true";
//		}
		
		Cookie bg_Cookie = new Cookie("bg_color", bg_color);
		response.addCookie(bg_Cookie);
		
		Cookie text_Cookie = new Cookie("text_color",text_color);
		response.addCookie(text_Cookie);
		
		Cookie bold_Cookie = new Cookie("bold",bold_Text);
		response.addCookie(bold_Cookie);
		
		Cookie italic_Cookie = new Cookie("italic",italic_Text);
		response.addCookie(italic_Cookie);
		
		Cookie textSize_Cookie = new Cookie("size",textSize);
		response.addCookie(textSize_Cookie);
		
		response.sendRedirect("GetCookieServlet");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
