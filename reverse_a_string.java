import java.util.*;
class reverse_a_string//to reverse a String
{
    public static void main(String args[])
    {
        System.out.println("Enter String");
        Scanner ss=new Scanner(System.in);
        String s=ss.nextLine(); 
        StringBuffer str=new StringBuffer(s);
        str.reverse();
        System.out.println(str);
    }
}
