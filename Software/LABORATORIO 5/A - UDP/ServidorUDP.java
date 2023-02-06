import java.net.*;
import java.io.*;
import java.text.SimpleDateFormat;  
import java.util.Date;  

public class ServidorUDP {

  public static void main (String args[]) {

    try {

      DatagramSocket socketUDP = new DatagramSocket(6789);
      byte[] bufer = new byte[1000];

      while (true) {
        // Construimos el DatagramPacket para recibir peticiones
        DatagramPacket peticion =
          new DatagramPacket(bufer, bufer.length);

        // Leemos una petici�n del DatagramSocket
        socketUDP.receive(peticion);
        SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");  
        Date date = new Date();  
        System.out.print("Datagrama recibido del host: " + peticion.getAddress());
        System.out.println(" desde el puerto remoto: " + peticion.getPort());
        System.out.print("El mensaje llegó a las: "+ formatter.format(date));

        // Construimos el DatagramPacket para enviar la respuesta
        DatagramPacket respuesta =
          new DatagramPacket(peticion.getData(), peticion.getLength(),peticion.getAddress(), peticion.getPort());

        // Enviamos la respuesta, que es un eco
        socketUDP.send(respuesta);
      }

    } catch (SocketException e) {
      System.out.println("Socket: " + e.getMessage());
    } catch (IOException e) {
      System.out.println("IO: " + e.getMessage());
    }
  }

}