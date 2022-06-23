# Flowchart

## Contents <a name="contents"></a>
- [play_video()](#play_video)
- [process_func()](#process_func)


## Flowchart

<a name="play_video"></a>
- `play_video()`
    ```mermaid
    flowchart TD
        B([ Start ]);
        E([ End ]);
        I1[/ Source, process_func, isSave, isLoop /];
        I2[/ Read Video /];
        D1{ isSave? };
        P2[ Define Writer ];
        D2{ Can Open Captured Video? };
        O1[/ Exit Message /];
        D3{ While True };
        I3[[ Read Frame-by-Frame ]];
        P3[[ Resize Frame ]];
        D4{ isLoop? };
        P4[ Reset frame_counter ];
        F1[[ Run process_func ]];
        F2[[ Get FPS ]];
        F3[[ Write FPS to File ]];
        F4[[ Put Information Text to Frame ]];
        D5{ isSave? };
        P5[ Write Frame to Video File ];
        P6[ Show Frame ];
        D6[/ Input 'q'? /];
        P7[ Release Video ];
        P8[ Destroy All Windows ];
        B --> I1;
        I1 --> I2;
        I2 --> D1;
        D1 -- Y --> P2 --> D2;
        D1 -- N --> D2;
        D2 -- Y --> D3;
        D2 -- N --> O1 --> E;
        D3 -- Y --> I3;
        D3 -- N --> P6;
        I3 -- Y --> P3 --> D4;
        I3 -- N --> E;
        D4 -- Y --> P4 --> F1;
        D4 -- N --> F1;
        F1 --> F2;
        F2 --> F3;
        F3 --> F4;
        F4 --> D5;
        D5 -- Y --> P5 --> P6;
        D5 -- N --> P6;
        P6 --> D6;
        D6 -- Y --> P7;
        D6 -- N --> D3;
        P7 --> P8;
        P8 --> E;
    ```

<br/>
<br/>

<a name="process_func"></a>
- `process_func()`: run image processing for single frame
    ```mermaid
    flowchart TD
        B([ Start ]);
        E([ End ]);
        I1[/ Read Frame & Shape /];
        F1[[ Determine ROI ]];
        F2[[ Convert BGR to HSV ]];
        F3[[ Blurring ]];
        F4[[ Color Thresholding ]];
        F5[[ Morphological Transformation ]];
        F6[[ Get Contours ]];
        F7[[ Get Centroid Point ]];
        F8[[ Write Data to File ]];
        O1[/ JSON File /];
        F9[[ Put Processed ROI to Frame ]];
        O2[/ Frame /];
        B --> I1;
        I1 --> F1;
        F1 --> F2;
        F2 --> F3;
        F3 --> F4;
        F4 --> F5;
        F5 --> F6;
        F6 --> F7;
        F7 --> F8;
        F8 --> O1;
        F8 --> F9;
        F9 --> O2;
        O2 --> E;
    ```
<br/>
<br/>
