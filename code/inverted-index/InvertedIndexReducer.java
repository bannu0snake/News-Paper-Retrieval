package InvertedIndex;
import java.io.IOException;
import java.util.*;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;

public class InvertedIndexReducer extends MapReduceBase implements Reducer<Text, Text, Text, Text> {
	public void reduce(Text t_key, Iterator<Text> values, OutputCollector<Text,Text> output, Reporter reporter) throws IOException {
		HashMap<String, Integer> postings = new HashMap<>();
		int sum = 0;
		while(values.hasNext()) {
			String val = values.next().toString();
			if(postings.containsKey(val)) {
				sum = postings.get(val) + 1;
				postings.put(val, sum);
			} else {
				postings.put(val, 1);
			}
		}
		Map<String, Integer> map = new TreeMap<>(postings);
		String temp = "";
		for(Map.Entry<String, Integer> entry: map.entrySet()) {
			String doc_key = entry.getKey();
			Integer freq_value = entry.getValue();
			temp += " " + doc_key + " " + freq_value;
		}
		output.collect(t_key, new Text(temp));
	}
}