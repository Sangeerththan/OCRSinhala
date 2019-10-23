import java.awt.Color;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.nio.file.*;
import java.util.*;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;





public class CharacterToGraphics {

    public static void main(String[] args) throws IOException  {
		
		String fileName = "characters.txt";
		List<String> dicList=new ArrayList<String>();  
		
		dicList = readUsingBufferedReader(fileName, StandardCharsets.UTF_8);
				

        /*
           Because font metrics is based on a graphics context, we need to create
           a small, temporary image so we can ascertain the width and height
           of the final image
         */
		for(String s:dicList){ 
			String text = s;
  
			BufferedImage img = new BufferedImage(1, 1, BufferedImage.TYPE_INT_ARGB);
			Graphics2D g2d = img.createGraphics();
			Font font = new Font("Nirmala UI", Font.PLAIN, 48);
			g2d.setFont(font);
			
			FontMetrics fm = g2d.getFontMetrics();
			int width = fm.stringWidth(text);
			int height = fm.getHeight();
			//add margine
			width = width+4;
			height=height+4;
			System.out.println(width);
			System.out.println(height);
			
			g2d.dispose();

			img = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);
			g2d = img.createGraphics();
			g2d.setColor(Color.WHITE);
			g2d.fillRect(0, 0, width, height);
			g2d.setRenderingHint(RenderingHints.KEY_ALPHA_INTERPOLATION, RenderingHints.VALUE_ALPHA_INTERPOLATION_QUALITY);
			g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
			g2d.setRenderingHint(RenderingHints.KEY_COLOR_RENDERING, RenderingHints.VALUE_COLOR_RENDER_QUALITY);
			g2d.setRenderingHint(RenderingHints.KEY_DITHERING, RenderingHints.VALUE_DITHER_ENABLE);
			g2d.setRenderingHint(RenderingHints.KEY_FRACTIONALMETRICS, RenderingHints.VALUE_FRACTIONALMETRICS_ON);
			g2d.setRenderingHint(RenderingHints.KEY_INTERPOLATION, RenderingHints.VALUE_INTERPOLATION_BILINEAR);
			g2d.setRenderingHint(RenderingHints.KEY_RENDERING, RenderingHints.VALUE_RENDER_QUALITY);
			g2d.setRenderingHint(RenderingHints.KEY_STROKE_CONTROL, RenderingHints.VALUE_STROKE_PURE);
			g2d.setFont(font);
			fm = g2d.getFontMetrics();
			g2d.setColor(Color.BLACK);
			g2d.drawString(text, 0, fm.getAscent());
			g2d.dispose();
			try {
				ImageIO.write(img, "png", new File("Output/"+text+".png"));
				//ImageIO.write(img, "png", new File(text+".png"));
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}

    }
	
	private static List readUsingBufferedReader(String fileName, Charset cs) throws IOException {
		File file = new File(fileName);
		FileInputStream fis = new FileInputStream(file);
		InputStreamReader isr = new InputStreamReader(fis, cs);
		BufferedReader br = new BufferedReader(isr);
		List<String> wordsList=new ArrayList<String>();  
		String line;
		System.out.println("Read text file using InputStreamReader");
		while((line = br.readLine()) != null){
			//process the line
			System.out.println(line);
			wordsList.add(line);
		}
		br.close();
		return wordsList;
	}

}