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
        D3{ while True };
        I3[/ Read Frame-by-Frame /];
        P3[ Resize Frame ];
        D3{ isLoop? };
        P4[ Reset frame_counter ];
        F1[[ Run process_func ]];
        F2[[ Get FPS ]];
        F3[[ Write FPS to File ]];
        F4[[ Put Information Text to Frame ]];
        D4{ isSave? };
        P4[ Write Frame to Video File ];
        P5[ Show Frame ];
        I4[/ Input 'q' /];
        P6[ Release Captured Video ];
        P7[ Destroy All Windows ];
        B --> I1;
        
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
