import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;


public class Main {

    private static String[] macro_split(String text){
        String[] split_strings = text.split("(\\w+)");
        return split_strings;
    }

    public static void main(String[] args) {
        // BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        // Request for user input
        String NSP_manifesto = PdfUtil.parsePdfFromDoc(PdfUtil.loadPDF(PdfUtil.getFile(PdfUtil.getPdfPath())));
        String[] words = macro_split(NSP_manifesto);
        System.out.println(words);
        System.exit(0);
    }
}
