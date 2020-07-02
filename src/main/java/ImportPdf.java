import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.nio.file.Path;
import java.util.Scanner;

import org.apache.pdfbox.pdmodel.PDDocument;

/**
 * ImportPdf
 */
public class ImportPdf {

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

    public static String getPdfPath() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter PDF path:");
        return scanner.nextLine();
    }
}
