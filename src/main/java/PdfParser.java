import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Scanner;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;

/**
 * PdfUtil
 */
public class PdfParser {
    private static Scanner scanner = new Scanner(System.in);

    private String pdfPathString;
    private Path pdfPath;
    private Path pdfStringsPath;
    private PDDocument pdfDocument;

    /**
     * Sets this {@link PdfParser}'s {@code pdfPathString}, {@code pdfPath} and
     * {@code pdfDocument} from the provided path string.
     *
     * @param pdfPathString A {@link String} representation of a PDF file path.
     */
    public PdfParser(String pdfPathString) {
        this.pdfPathString = pdfPathString;
        this.pdfPath = Path.of(this.pdfPathString, "");

        try {
            this.pdfDocument = PDDocument.load(this.pdfPath.toFile());
        } catch (IOException e) {
            System.err.println(e);
            System.out.println("PDF file failed to load; using empty file.");

            this.pdfDocument = new PDDocument();
        }
    }

    /**
     * 
     * @return
     */
    public static PdfParser readPdfPath() {
        System.out.println("Enter PDF file path: ");
        return new PdfParser(scanner.nextLine());
    }

    /**
     * 
     * @return
     */
    public boolean setOutputFile() {
        System.out.println("Enter file output path: ");
        this.pdfStringsPath = Path.of(scanner.nextLine(), "");

        try {
            Files.createFile(this.pdfStringsPath);
            return true;
        }
        catch (FileAlreadyExistsException e) {
            System.err.println(e);
            System.out.println("File already exists.");
            return false;
        }
         catch (IOException e) {
            System.err.println(e);
            System.out.println("File could not be created. Check permissions.");
            return false;
        }
    }

    public String getPdfStrings() {
        try {
            return new PDFTextStripper().getText(this.pdfDocument);
        } catch (IOException e) {
            System.err.println(e);
            System.out.println("Unable to read PDF. Returning empty string.");

            return "";
        }
    }

    public void writeStringToFile(String string) {
        try (BufferedWriter writer = Files.newBufferedWriter(pdfStringsPath, Charset.forName("UTF-8"))) {
            writer.append(string).flush();
        } catch (Exception e) {
            System.err.println(e);
            System.out.println("Could not write to file.");
        }
    }

    public String getPdfPathString() {
        return pdfPathString;
    }

    public Path getPdfStringsPath() {
        return pdfStringsPath;
    }

    public Path getPdfPath() {
        return pdfPath;
    }

    public PDDocument getPdfDocument() {
        return pdfDocument;
    }
}