import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sales {
    public static void main(String[] args) throws Exception {
        File file=null;
        
        BufferedReader in= new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the filename from which data has to be parsed");
        String filename=in.readLine();
        try {
            file = new File(filename);
            if(!file.exists())
                file.createNewFile();
            while(true) {
                    System.out.println("Enter the name of Client: ");
                    String client=in.readLine();
                    System.out.println("Enter the Service category sold: ");
                    String Category=in.readLine();
                    System.out.println("Enter the amount of the sale: ");
                    String amount=in.readLine();
                    System.out.println("Please enter the date in the correct format(dd/MM/yyyy)");
                    String date=in.readLine();
                    String value= client+";"+Category+";"+amount+";"+date;
                    System.out.println(value);
                    FileWriter fr = new FileWriter(file, true);
                    BufferedWriter bw = new BufferedWriter(fr);
                    bw.write("\n"+value);
                    
                    bw.close();
                    System.out.println("Do you want to input more data(Y/N) ?");
                    String s=in.readLine();
                    System.out.println(s);
                    if(s.equals("N"))
                        break;
            }
            
           
        } 
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        catch(IOException e) {
            e.printStackTrace();
        }
//        finally {
//            br.close();
//        }
    }
}