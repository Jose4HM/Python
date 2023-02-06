import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Servidor {

    public static void main(String[] args) {

        ServerSocket servidor = null;
        Socket sc = null;
        DataInputStream in;
        DataOutputStream out;

        //puerto de nuestro servidor
        final int PUERTO = 5000;

        try {
            //Creamos el socket del servidor
            servidor = new ServerSocket(PUERTO);
            System.out.print("----------Servidor escuchando por el puerto :");
            System.out.print(PUERTO);
            System.out.print("----------");
            //Siempre estara escuchando peticiones
            while (true) {

                //Espero a que un cliente se conecte
                sc = servidor.accept();

                System.out.println("Client conected");
                in = new DataInputStream(sc.getInputStream());
                out = new DataOutputStream(sc.getOutputStream());

                //Leo el mensaje que me envia
                String mensaje = in.readUTF();
                // System.out.println(mensaje);
                int nbr=0;
                //Convierto a numeros
                try{
                    nbr = Integer.parseInt(mensaje);
                    System.out.println(nbr); // output = 25
                }
                catch (NumberFormatException ex){
                    ex.printStackTrace();
                }
                //Suma
                // int number=String.valueOf(mensaje).length();  
                int number=nbr;
                int digit,sum=0;
                while(number > 0)  
                {  
                //finds the last digit of the given number    
                digit = number % 10;  
                //adds last digit to the variable sum  
                sum = sum + digit;  
                //removes the last digit from the number  
                number = number / 10;  
                }  

                //Le envio un mensaje
                out.writeUTF("La suma es:"+sum);
                String mensaje2 = in.readUTF();
                System.out.println(mensaje2);
                //Cierro el socket
                sc.close();
                System.out.println("Client disconected");

            }

        } catch (IOException ex) {
            Logger.getLogger(Servidor.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

}