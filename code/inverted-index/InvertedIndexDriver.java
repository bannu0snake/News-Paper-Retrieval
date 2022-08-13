package InvertedIndex;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;
import java.io.IOException;
import org.apache.hadoop.fs.Path;

public class InvertedIndexDriver {
    public static void main(String[] args) throws IOException {
        JobClient my_client = new JobClient();
        JobConf job_conf = new JobConf(InvertedIndexDriver.class);
        job_conf.setJobName("Inverted Index");
        job_conf.setOutputKeyClass(Text.class);
        job_conf.setOutputValueClass(Text.class);
        job_conf.setMapperClass(InvertedIndex.InvertedIndexMapper.class);
        job_conf.setReducerClass(InvertedIndex.InvertedIndexReducer.class);
        job_conf.setInputFormat(TextInputFormat.class);
        job_conf.setOutputFormat(TextOutputFormat.class);
        FileInputFormat.setInputPaths(job_conf, new Path(args[0]));
        FileOutputFormat.setOutputPath(job_conf, new Path(args[1]));
        my_client.setConf(job_conf);
        try {
            JobClient.runJob(job_conf);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}