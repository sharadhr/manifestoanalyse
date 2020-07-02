import java.io.IOException;
import java.nio.file.Path;
import java.util.Scanner;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;

/**
 * PdfUtil
 */
public class PdfUtil {

    /**
     * 
     * @param pathString
     * @return
     */
    public static Path getFile(String pathString) {
        return Path.of(pathString, "");
    }

    /**
     * 
     * @param path
     * @return
     */
    public static PDDocument loadPDF(Path path) {
        try {
            return PDDocument.load(path.toFile());
        } catch (IOException e) {
            System.err.println(e);
            System.err.println("The PDF document was not loaded. Created an empty PDF.");
            return new PDDocument();
        }
    }

    /**
     * 
     * @return
     */
    public static String getPdfPath() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter PDF path:");
        return scanner.nextLine();
    }

    /**
     * 
     * @param pdf
     */
    public static String parsePdfFromDoc(PDDocument pdfdoc) {
        try {
            return new PDFTextStripper().getText(pdfdoc);
        } catch (IOException e) {
            System.err.println("Failed to read text. Returning empty string.");
            return "";
        }
    }
}
