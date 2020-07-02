import java.util.LinkedList;

public class StringSplit {
    String bigpara;
    public StringSplit(String text){
        bigpara = text;
        String[] split_strings = macro_split();
    }

    private String[] macro_split(){
        String[] split_strings = this.bigpara.split("(\\w+)");
        return split_strings;
    }

    
    
}