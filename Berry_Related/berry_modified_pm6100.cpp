// C/C++ code to provide data export functionality for BerryMed.
// by oca-john@hotmail.com

// This source code is not a complete compilable project and you will need to 
// obtain the complete code from the BerryMed vendor first.
// If you have obtained the source code, install the Microsoft Visual C++ 6.0 
// development environment on windows xp/7. And then import the vendor supplied 
// source code project into the development environment. 
// Integrate the code from this file into the vendor's code project, and 
// recompile it as an executable file.


// The following header files are additionally required.
#include "windows.h"
#include "stdio.h"
#include "time.h"
#include "string.h"


// Set the file handles for the various data to export.
FILE *fspo;     // SPO2 Wave
FILE *frsp;     // RESP Wave
FILE *fhr;      // Heart Rate
FILE *fspv;     // SPO2 Sat
FILE *fprt;     // Pulse Rate


// The function block that needs to be modified for data export.
void CMainFrame::ParsePackage(UCHAR *pkgData, UINT pkgLength)
{
    // The vendor code for initialising variables and getting timestamps 
    // is omitted here.

    // Processing of packets and export to file.
    pkgType = pkgData[3];
    switch (pkgType) {
        case PKG_SPO2_WAVE:
            // The vendor code for extracting the blood oxygen waveform from 
            // the data block is omitted here.
            fspo = fopen("spo_data.csv", "a");
            fprintf(fspo, "%04d-%02d-%02d %02d:%02d:%02d.%03d,", 
                    t.wYear, t.wMonth, t.wDay, t.wHour, 
                    t.wMinute, t.wSecond, t.wMilliseconds);
            fprintf(fspo, "%-5d\n", m_SPO2Wave);
            fclose(fspo);
            break;
        case PKG_RESP_WAVE:
            // The vendor code for extracting the respiratory waveform from 
            // the data block is omitted here.
            frsp = fopen("rsp_data.csv", "a");
            fprintf(frsp, "%04d-%02d-%02d %02d:%02d:%02d.%03d,", 
                    t.wYear, t.wMonth, t.wDay, t.wHour, 
                    t.wMinute, t.wSecond, t.wMilliseconds);
            fprintf(frsp, "%-5d\n", m_RESPWave);
            fclose(frsp);
            break;
        case PKG_ECG_PARAM:
            // The vendor code for extracting the heart rate data from the 
            // data block is omitted here.
            fhr = fopen("hr_data.csv", "a");
            fprintf(fhr, "%04d-%02d-%02d %02d:%02d:%02d.%03d,", 
                    t.wYear, t.wMonth, t.wDay, t.wHour, 
                    t.wMinute, t.wSecond, t.wMilliseconds);
            fprintf(fhr, "%-3d\n", m_HeartRate);
            fclose(fhr);
            break;
        case PKG_SPO2:
            // The vendor code for extracting oxygen saturation and pulse 
            // rate data from the data block is omitted here.
            fspv = fopen("spv_data.csv", "a");
            fprintf(fspv, "%04d-%02d-%02d %02d:%02d:%02d.%03d,", 
                    t.wYear, t.wMonth, t.wDay, t.wHour, 
                    t.wMinute, t.wSecond, t.wMilliseconds);
            fprintf(fspv, "%-3d\n", m_SPO2Sat);
            fclose(fspv);
            fprt = fopen("prt_data.csv", "a");
            fprintf(fprt, "%04d-%02d-%02d %02d:%02d:%02d.%03d,", 
                    t.wYear, t.wMonth, t.wDay, t.wHour, 
                    t.wMinute, t.wSecond, t.wMilliseconds);
            fprintf(fprt, "%-3d\n", m_PulseRate);
            fclose(fprt);
            break;
        
        // There are other blocks of code in the vendor's source code here.
    }
}
