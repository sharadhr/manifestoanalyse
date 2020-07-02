import java.util.Iterator;
import java.util.LinkedList;

public class sorting{
    public sorting(String text){
        String word = text;
        String type;
    }

    private int pronoun(String text){
        LinkedList<String> pronouns = new LinkedList<String>();
        pronouns.add("i"); pronouns.add("me"); pronouns.add("me"); pronouns.add("mine"); pronouns.add("myself");
        pronouns.add("you"); pronouns.add("your"); pronouns.add("yourself"); 
        pronouns.add("he"); pronouns.add("him"); pronouns.add("his"); pronouns.add("himself");
        pronouns.add("she"); pronouns.add("her"); pronouns.add("hers"); pronouns.add("herself");
        pronouns.add("it"); pronouns.add("its"); pronouns.add("it's"); pronouns.add("itself");
        pronouns.add("we"); pronouns.add("us"); pronouns.add("our"); pronouns.add("ours"); pronouns.add("ourselves");
        pronouns.add("yourselves"); 
        pronouns.add("they"); pronouns.add("them"); pronouns.add("their"); pronouns.add("theirs");
        pronouns.add("their's"); pronouns.add("themselves");
        text = text.toLowerCase();
        for(Iterator<E> i = pronouns.iterator(); i.hasNext();){
            String word = i.next();
            if(word == text){
                type = "Pronoun";
                return 1;
            }
            else{
                return 0;
            }
        }
    }

    private int preposition(String text){
        LinkedList<String> prepositions = new LinkedList<String>(); 
        prepositions.add("in"); prepositions.add("on"); prepositions.add("at");
        prepositions.add("for"); prepositions.add("by");
        for(Iterator<E> i = prepositions.iterator(); i.hasNext();){
            String word = i.next();
            if(word == text){
                type = "Preposition";
                return 1;
            }
            else{
                return 0;
            }
        }
    }

    private int conjunction(String text){
        LinkedList<String> conjunctions = new LinkedList<String>(); 
        conjunctions.add("and"); conjunctions.add("nor");
        return 1;
    }
}