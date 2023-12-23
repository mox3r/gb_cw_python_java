import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Writer2Txt {
    final String fname;

    public Writer2Txt() {
        this.fname = currentDateToFileName() + ".txt";
    }

    private String currentDateToFileName() {
        Date date = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat("YYYYMMDDHHmm");

        return String.format("%sMSK", sdf.format(date.getTime()));
    }

    public void write(Toy t) {
        try (FileWriter writer = new FileWriter(fname, true)) {
            writer.write("Поздравляем! Вы выиграли игрушку " + t.getName() + "!\n");
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
