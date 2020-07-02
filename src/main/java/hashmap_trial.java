import java.util.HashMap;

public class hashmap_trial {
    HashMap<String, Integer> word_count = new HashMap<String, Integer>();
    HashMap<String, Integer> pronouns = new HashMap<String, Integer>();
    HashMap<String, Integer> prepositions = new HashMap<String, Integer>();
    HashMap<String, Integer> conjunctions = new HashMap<String, Integer>();
    HashMap<String, Integer> quantifiers = new HashMap<String, Integer>();
    HashMap<String, Integer> articles = new HashMap<String, Integer>();

    
    public hashmap_trial(String text){
        init_word_cat();
    }

    private void init_word_cat(){
        pronouns.put("i", 0); pronouns.put("me", 0); pronouns.put("me", 0); pronouns.put("mine", 0); pronouns.put("myself", 0);
        pronouns.put("you", 0); pronouns.put("your", 0); pronouns.put("yourself", 0); 
        pronouns.put("he", 0); pronouns.put("him", 0); pronouns.put("his", 0); pronouns.put("himself", 0);
        pronouns.put("she", 0); pronouns.put("her", 0); pronouns.put("hers", 0); pronouns.put("herself", 0);
        pronouns.put("it", 0); pronouns.put("its", 0); pronouns.put("it's", 0); pronouns.put("itself", 0);
        pronouns.put("we", 0); pronouns.put("us", 0); pronouns.put("our", 0); pronouns.put("ours", 0); pronouns.put("ourselves", 0);
        pronouns.put("yourselves", 0); 
        pronouns.put("they", 0); pronouns.put("them", 0); pronouns.put("their", 0); pronouns.put("theirs", 0);
        pronouns.put("their's", 0); pronouns.put("themselves", 0);

        prepositions.put("in", 0); prepositions.put("on", 0); prepositions.put("at", 0);
        prepositions.put("for", 0); prepositions.put("by", 0); prepositions.put("from", 0); prepositions.put("with", 0);
        prepositions.put("to", 0); prepositions.put("about", 0); prepositions.put("below", 0); prepositions.put("over", 0); prepositions.put("above", 0);

        conjunctions.put("and" ,0); conjunctions.put("nor" ,0); conjunctions.put("but", 0); conjunctions.put("or", 0); conjunctions.put("yet", 0);
        conjunctions.put("so", 0); conjunctions.put("either", 0); conjunctions.put("neither", 0); conjunctions.put("not only", 0); conjunctions.put("whether", 0);

        quantifiers.put("many", 0); quantifiers.put("few", 0); quantifiers.put("some", 0); quantifiers.put("every", 0); quantifiers.put("a lot of", 0);
        quantifiers.put("any", 0); quantifiers.put("less", 0);

        articles.put("a", 0); articles.put("an", 0); articles.put("the", 0); articles.put("whose", 0); quantifiers.put("all", 0); 
    }

    public void put_word(String text){
        text = text.toLowerCase();
        if(word_count.containsKey(text) == true){
            word_count.put(text, word_count.get(text) + 1);
        }
        else{
            word_count.put(text, 1);
        }
    }

    
}