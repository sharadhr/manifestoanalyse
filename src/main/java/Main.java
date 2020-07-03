public class Main {

    public static void main(String[] args) {

        // Get PDF document path from user
        PdfParser parser = PdfParser.readPdfPath();
        parser.setOutputFile();

        String NSP_manifesto = parser.getPdfStrings();

        parser.writeStringToFile(NSP_manifesto);
        System.exit(0);
    }
}
