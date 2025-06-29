// SemanticAnalyzer.java
import java.io.*;
import java.util.*;
import org.json.*;

public class SemanticAnalyzer {
    public static void main(String[] args) throws Exception {
        String json = new String(Files.readAllBytes(new File(args[0]).toPath()));
        JSONArray ast = new JSONArray(json);

        Set<String> declaredVars = new HashSet<>();

        for (int i = 0; i < ast.length(); i++) {
            JSONArray node = ast.getJSONArray(i);
            String type = node.getString(0);

            if (type.equals("assign")) {
                declaredVars.add(node.getString(1));
            } else if (type.equals("print")) {
                String var = node.getString(1);
                if (!declaredVars.contains(var) && !var.matches("\\d+")) {
                    System.err.println("Semantic Error: Undeclared variable " + var);
                    System.exit(1);
                }
            }
        }

        System.out.println("Semantic check passed.");
    }
}

