import java.util.ArrayList;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.Group;
import javafx.stage.Stage;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;
import javafx.scene.control.ScrollPane;

public class Display extends Application{
    private String product;
    private String description;
    private String userInput;
    private ArrayList<String> founders;
    private String patentNum;
    private String orgin;
    private String status;

    @Override
    public void start(Stage primaryStage) throws Exception{
        
    }
    
    public static void main(String[] args){
        launch(args);
    }
}