import java.util.*;
class demo//to reverse a String
{
    public static void main(String args[])
    {
        System.out.println("This is a demo program");
        Scanner ss=new Scanner(System.in);
        String s=ss.nextLine(); 
        StringBuffer str=new StringBuffer(s);
        str.reverse();
        System.out.println(str);
    }
}
