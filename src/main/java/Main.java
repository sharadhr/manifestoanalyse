import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class Main {

    private static String[] macro_split(String text){
        String[] split_strings = text.split("(\\W+)");
        return split_strings;
    }

    public static void main(String[] args) {
        // BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        // Request for user input
        String NSP_manifesto = PdfUtil.parsePdfFromDoc(PdfUtil.loadPDF(PdfUtil.getFile(PdfUtil.getPdfPath())));
        String[] words = macro_split(NSP_manifesto);
        hashmap_trial trial = new hashmap_trial(words);
        HashMap<String, Integer> results = trial.returnWordcount();
        for (Entry entry : results.entrySet())
        {
            System.out.println("key: " + entry.getKey() + "; value: " + entry.getValue());
        }
        //System.out.println(List.of(words));
        System.exit(0);
    }
}
