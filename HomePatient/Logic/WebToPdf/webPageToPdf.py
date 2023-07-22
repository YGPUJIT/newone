import pdfkit
from datetime import date

path_wkthmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)


def htmlToPdfApi(patient, age, city, patientid, medicines,doctor, specilisation, date):
    medicines_arr=[]
    for index,med in enumerate(medicines):
        p="<p style='font-size: 14px; line-height: 140%;'><span style='font-family: 'courier new', courier; font-size: 14px; line-height: 19.6px;'><strong>Medicine "+str(index+1)+":</strong> " +med['medicine_name'].upper()+"</span></p>"
        medicines_arr.append(p)
    medicine=' '.join(medicines_arr)
    string = '''
    <!doctype html>
<html>

<head>
  <meta charset="utf-8">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title></title>
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  
  


  


</head>

<body style="width:700px; margin:auto">

  <div id="u_body" class="u_body" style="min-height: 100vh; background-color: #e7e7e7; font-family: arial,helvetica,sans-serif;">

    <div id="u_row_5" class="u_row" style="background-color: #ffffff; padding: 0px;">
      <div class="container" style="margin: 0 auto;">
        <div class="u-row" style="display: flex;flex-wrap: nowrap;margin-left: 0;margin-right: 0;">

          <div id="u_column_6" class="u-col u-col-100 u_column" style="position: relative;width: 100%;padding-right: 0;padding-left: 0;flex: 0 0 100%;max-width: 100%;">
            <div style="padding: 0px;background-color:#ffffff;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

              <div id="u_content_text_1" class="u_content_text" style="overflow-wrap: break-word;padding: 10px;">

                <div style="color: #000000; line-height: 140%; text-align: left; word-wrap: break-word;">

                </div>

              </div>

            </div>
          </div>

        </div>
      </div>
    </div>

    <div id="u_row_6" class="u_row" style="background-color: #ffffff; padding: 0px;">
      <div class="container" style="margin: 0 auto;">
        <div class="u-row" style="display: flex;flex-wrap: nowrap;margin-left: 0;margin-right: 0;">

          <div id="u_column_7" class="u-col u-col-100 u_column" style="position: relative;width: 100%;padding-right: 0;padding-left: 0;flex: 0 0 100%;max-width: 100%;">
            <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

              <div id="u_content_text_2" class="u_content_text" style="overflow-wrap: break-word;padding: 10px;">

                <div style="color: #000000; line-height: 140%; text-align: left; word-wrap: break-word;">

                </div>

              </div>

            </div>
          </div>

        </div>
      </div>
    </div>

    <div id="u_row_3" class="u_row" style="background-color: #236fa1; padding: 0px;">
      <div class="container" style="margin: 0 auto;">
        <div class="u-row" style="display: flex;flex-wrap: nowrap;margin-left: 0;margin-right: 0;">

          <div id="u_column_3" class="u-col u-col-100 u_column" style="position: relative;width: 100%;padding-right: 0;padding-left: 0;flex: 0 0 100%;max-width: 100%;">
            <div style="padding: 0px;background-color:#236fa1;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

              <div id="u_content_heading_1" class="u_content_heading" style="overflow-wrap: break-word;padding: 20px 10px 21px;">

                <h1 style="margin: 0px; color: #ffffff; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: 'Montserrat',sans-serif; font-size: 24px;">
                  Prescription
                </h1>

              </div>

            </div>
          </div>

        </div>
      </div>
    </div>

    <div id="u_row_8" class="u_row" style="background-color: #ffffff; padding: 0px;">
      <div class="container" style="margin: 0 auto;">
        <div class="u-row" style="display: flex;flex-wrap: nowrap;margin-left: 0;margin-right: 0;">

          <div id="u_column_9" class="u-col u-col-100 u_column" style="position: relative;width: 100%;padding-right: 0;padding-left: 0;flex: 0 0 100%;max-width: 100%;">
            <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

              <div id="u_content_text_4" class="u_content_text" style="overflow-wrap: break-word;padding: 10px;">

                <div style="color: #000000; line-height: 140%; text-align: left; word-wrap: break-word;">

                </div>

              </div>

            </div>
          </div>

        </div>
      </div>
    </div>

    <div id="u_row_4" class="u_row" style="background-color: #ffffff; padding: 0px;">
      <div class="container" style="margin: 0 auto;">
        <div class="u-row" style="display: flex;flex-wrap: nowrap;margin-left: 0;margin-right: 0;">

          <div id="u_column_5" class="u-col u-col-100 u_column" style="position: relative;width: 100%;padding-right: 0;padding-left: 0;flex: 0 0 100%;max-width: 100%;">
            <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

              <div id="u_content_divider_3" class="u_content_divider" style="overflow-wrap: break-word;padding: 5px;">
                <div style="text-align:center;line-height:0">
                  <div style="border-top-width:4px;border-top-style:solid;border-top-color:#236fa1;width:100%;display:inline-block;line-height:4px;height:0px;vertical-align:middle"> </div>
                </div>
              </div>

            </div>
          </div>

        </div>
      </div>
    </div>

    <div id="u_row_10" class="u_row" style="background-color: #ffffff; padding: 0px;">
      <div class="container" style="margin: 0 auto;">
        <div class="u-row" style="display: flex;flex-wrap: nowrap;margin-left: 0;margin-right: 0;">

          <div id="u_column_11" class="u-col u-col-50 u_column" style="position: relative;width: 100%;padding-right: 0;padding-left: 0;flex: 0 0 50%;max-width: 50%;">
            <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

              <div id="u_content_text_5" class="u_content_text" style="overflow-wrap: break-word;padding: 10px;">

                <div style="color: #000000; line-height: 140%; text-align: left; word-wrap: break-word;">
                        <p style="font-size: 14px; line-height: 140%;"><span style="font-family: georgia, palatino; font-size: 14px; line-height: 19.6px;">Dr. '''+doctor+'''</span></p>
                        <p style="font-size: 14px; line-height: 140%;"><span style="font-family: georgia, palatino; font-size: 14px; line-height: 19.6px;">'''+specilisation + '''</span></p>
                        <p style="font-size: 14px; line-height: 140%;"><span style="font-family: georgia, palatino; font-size: 14px; line-height: 19.6px;">Ph: 1234567890</span></p>
                </div>

              </div>

            </div>
          </div>

          <div id="u_column_12" class="u-col u-col-50 u_column" style="position: relative;width: 100%;padding-right: 0;padding-left: 0;flex: 0 0 50%;max-width: 50%;">
            <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

              <div id="u_content_text_6" class="u_content_text" style="overflow-wrap: break-word;padding: 10px;">

                <div style="color: #000000; line-height: 140%; text-align: left; word-wrap: break-word;">
                        <p style="font-size: 14px; line-height: 140%;"><span style="font-family: georgia, palatino; font-size: 14px; line-height: 19.6px;"><strong>Patient ID:</strong> '''+patientid.upper()+'''</span></p>
                        <p style="font-size: 14px; line-height: 140%;"><span style="font-family: georgia, palatino; font-size: 14px; line-height: 19.6px;">Date:'''+date+'''</span></p>
                  <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
                </div>

              </div>

            </div>
          </div>

        </div>
      </div>
    </div>

    <div id="u_row_9" class="u_row" style="background-color: #ffffff; padding: 0px;">
      <div class="container" style="margin: 0 auto;">
        <div class="u-row" style="display: flex;flex-wrap: nowrap;margin-left: 0;margin-right: 0;">

          <div id="u_column_10" class="u-col u-col-100 u_column" style="position: relative;width: 100%;padding-right: 0;padding-left: 0;flex: 0 0 100%;max-width: 100%;">
            <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

              <div id="u_content_divider_1" class="u_content_divider" style="overflow-wrap: break-word;padding: 5px;">
                <div style="text-align:center;line-height:0">
                  <div style="border-top-width:4px;border-top-style:solid;border-top-color:#236fa1;width:100%;display:inline-block;line-height:4px;height:0px;vertical-align:middle"> </div>
                </div>
              </div>

            </div>
          </div>

        </div>
      </div>
    </div>

    <div id="u_row_15" class="u_row" style="background-color: #ffffff; padding: 0px;">
      <div class="container" style="margin: 0 auto;">
        <div class="u-row" style="display: flex;flex-wrap: nowrap;margin-left: 0;margin-right: 0;">

          <div id="u_column_17" class="u-col u-col-100 u_column" style="position: relative;width: 100%;padding-right: 0;padding-left: 0;flex: 0 0 100%;max-width: 100%;">
            <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

              <div id="u_content_text_8" class="u_content_text" style="overflow-wrap: break-word;padding: 10px;">

                <div style="color: #000000; line-height: 140%; text-align: left; word-wrap: break-word;">
                  <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
                    '''+medicine+'''
                  <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
                </div>

              </div>

            </div>
          </div>

        </div>
      </div>
    </div>

    <div id="u_row_9" class="u_row" style="background-color: #ffffff; padding: 0px;">
      <div class="container" style="margin: 0 auto;">
        <div class="u-row" style="display: flex;flex-wrap: nowrap;margin-left: 0;margin-right: 0;">

          <div id="u_column_10" class="u-col u-col-100 u_column" style="position: relative;width: 100%;padding-right: 0;padding-left: 0;flex: 0 0 100%;max-width: 100%;">
            <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

              <div id="u_content_divider_1" class="u_content_divider" style="overflow-wrap: break-word;padding: 5px;">
                <div style="text-align:center;line-height:0">
                  <div style="border-top-width:4px;border-top-style:solid;border-top-color:#236fa1;width:100%;display:inline-block;line-height:4px;height:0px;vertical-align:middle"> </div>
                </div>
              </div>

            </div>
          </div>

        </div>
      </div>
    </div>

    <div id="u_row_16" class="u_row" style="background-color: #ffffff; padding: 0px;padding-left:10px;font-family: arial,helvetica,sans-serif;padding-top:50px">
        <table style="width:50%;">
            <tr>
                <td>Patient name:</td>    
                <td>'''+patient+'''</td>
            </tr>
            <tr>
                    <td>Age:</td>    
                    <td>'''+age+'''</td>
            </tr>
            <tr>
                    <td>Address:</td>    
                    <td>'''+city+'''</td>
            </tr>
        </table>
    </div>

    <div id="u_row_11" class="u_row" style="background-color: #ffffff; padding: 0px;">
      <div class="container" style="margin: 0 auto;">
        <div class="u-row" style="display: flex;flex-wrap: nowrap;margin-left: 0;margin-right: 0;">

          <div id="u_column_13" class="u-col u-col-100 u_column" style="position: relative;width: 100%;padding-right: 0;padding-left: 0;flex: 0 0 100%;max-width: 100%;">
            <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

              <div id="u_content_text_12" class="u_content_text" style="overflow-wrap: break-word;padding: 10px;">

                <div style="color: #000000; line-height: 140%; text-align: left; word-wrap: break-word;">

                </div>

              </div>

            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</body>
</html>
'''
    return pdfkit.from_string(string,False, configuration=config)
