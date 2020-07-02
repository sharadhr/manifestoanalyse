import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;


public class Main {
    public static void main(String[] args) {
        // BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        // Request for user input
        System.out.println(PdfUtil.parsePdfFromDoc(PdfUtil.loadPDF(PdfUtil.getFile(PdfUtil.getPdfPath()))));

        System.exit(0);
    }
}
