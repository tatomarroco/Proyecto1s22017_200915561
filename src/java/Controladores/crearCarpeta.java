/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Controladores;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.MalformedURLException;
import java.net.URL;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 *
 * @author Estuardo
 */
@WebServlet(urlPatterns = {"/crearCarpeta"})
public class crearCarpeta extends HttpServlet{
 public static OkHttpClient webClient = new OkHttpClient();
    String r="";
    
    public static String error="";
    
    public static String carpetasString="";

    public static String getCarpetasString() {
        return carpetasString;
    }

    public static  void setCarpetasString(String carpetasString) {
        crearCarpeta.carpetasString = carpetasString;
    }
    

    public static String getError() {
        return error;
    }

    public static void setError(String error) {
        crearUsuario.error = error;
    }
    
    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    
    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException {
        String nombre = request.getParameter("nombre"); 
        
        HttpSession sesion = request.getSession(true);
               String user = sesion.getAttribute("sesionusuario").toString();
        
        /*Este codigo ve si los dos campos de contraseña que envia la pagina coinciden, si lo hacen envia user y password a Flask para crear usuario*/
        
            RequestBody formBody = new FormEncodingBuilder()
                .add("user",user)
                .add("nombre", nombre)
                .build();
            r = getString("crearCarpeta", formBody); 
            setCarpetasString(r);
        
            response.sendRedirect("drive.jsp");
    }
    
     public String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request req = new Request.Builder().url(url).post(formBody).build();
            Response resp = webClient.newCall(req).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = resp.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            //java.util.logging.Logger.getLogger(proyecto2.TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
            System.out.println(ex.getMessage());
        } catch (Exception ex) {
            //java.util.logging.Logger.getLogger(proyecto2.TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
        System.out.println(ex.getMessage());
        }
        return null;
    }
    

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return getCarpetasString();
    }// </editor-fold>
}
