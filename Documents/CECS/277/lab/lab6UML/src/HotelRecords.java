import java.io.*;

public class HotelRecords {
    public static void main(String[] args) throws Exception {
        File file=null;
        BufferedReader br=null;
        BufferedReader in= new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the filename from which data has to be parsed");
        String filename=in.readLine();
        
        try {
            file = new File(filename);
            
            br = new BufferedReader(new FileReader(file));

            String st;
            while ((st = br.readLine()) != null) {
                String input[] = st.split(";");
                System.out.println("Enter the path where you want to create the files");
                String path=in.readLine();
                
                if(input.length==4){
                        File f1 = new File(path +"\\"+ input[1] + ".txt");
                        if (!f1.exists())
                            f1.createNewFile();
                        FileWriter fr = new FileWriter(f1, true);
                        BufferedWriter bw = new BufferedWriter(fr);
                        bw.write(st+"\n");
                        bw.close();
                }
                else{
                        throw new UnknownTransaction("The format for the transaction is not known");
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        catch(UnknownTransaction e){
                System.out.println(e.getMessage());
        }
        catch(IOException e) {
            e.printStackTrace();
        }
        finally {
                
            br.close();
        }
    }
}
class UnknownTransaction extends Exception 
{ 
    public UnknownTransaction(String s) 
    { 
        super(s); 
    } 
}