//http://127.0.0.1:5000/



import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
        URL url = new URL("http://127.0.0.1:5000/answer");
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("POST");
        con.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
        con.setDoOutput(true);

        String para = "انا مصطفي صابر";
        String encoded = URLEncoder.encode(para, "UTF-8");

        DataOutputStream wr = new DataOutputStream(con.getOutputStream());
        wr.writeBytes(encoded);
        wr.flush();
        wr.close();

        BufferedReader in = null;
        String inputLine;
        StringBuilder body;

        in = new BufferedReader(new InputStreamReader(con.getInputStream(), Charset.forName("UTF-8")));

        body = new StringBuilder();

        while ((inputLine = in.readLine()) != null) {
            body.append(inputLine);
        }

        System.out.println(body.toString());
    }
}
