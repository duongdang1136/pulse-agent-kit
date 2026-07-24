---
id: "fpl-streaming-specifications-v1-1"
title: "Fpl Streaming Specifications V1.1"
type: "knowledge"
category: "Product"
project: "fptplay"
source_file: "fpl_streaming-specifications_v1.1.docx"
source_type: "docx"
updated_at: "2026-07-24"
checksum_sha256: "dcbf62ef503bb5a575b9ce5c3a1cbaad9126bd483c1278436900352cbbd53e03"
tags:
  - "fptplay"
---

# Fpl Streaming Specifications V1.1

> Imported from `fpl_streaming-specifications_v1.1.docx`. Treat this page as project evidence, not an automatically verified decision.

Tóm lược (abstract)

Tài liệu này mô tả chi tiết triển khai hệ thống streaming video dựa trên tiêu chuẩn HLS và DASH (MPEG-DASH), bao gồm các thông tin cần tổ chức như codecs, quản lý nhiều luồng âm thanh (audio tracks), phụ đề và bitrate ladder. Các khía cạnh như chọn lựa và chuyển đổi chất lượng video (rendition switching), cơ chế dự phòng (fallback mechanisms) cũng được đề cập. Ngoài ra, tài liệu còn trình bày về cách tổ chức manifest cùng các phương án và ví dụ triển khai cụ thể với HLS và DASH.

Disclaimer

This document and the information contained herein are intended solely for review by authorized companies. Communication of this material to third party is strictly prohibited. This document shall not be used as the basis for design or manufacture any products incorporating FPT Play Confidential Information without the express written consent of FPT Play and its partners in each case.

LỊCH SỬ THAY ĐỔI (DOCUMENT HISTORY)

Confidential level: privacy of enterprise

NHẬT KÝ THAY ĐỔI (CHANGE LOG)

NỘI DUNG (CONTENTS)

Page

LỊCH SỬ THAY ĐỔI (DOCUMENT HISTORY)	ii

DANH MỤC TỪ VIẾT TẮT (ABBREVIATIONS)	ix

DANH MỤC HÌNH ẢNH (LIST OF FIGURES)	xv

DANH MỤC BẢNG BIỂU (LIST OF TABLES)	xvi

1.	GIỚI THIỆU (INTRODUCTION)	1

1.1	Phạm vi và mục tiêu chính	1

1.2	Ký hiệu tuân thủ (conformance requirements/notation)	1

1.3	Tiêu chuẩn tham chiếu (reference standards)	1

2.	TỔNG QUAN VỀ STREAMING	3

2.1	Hệ sinh thái truyền hình (TV ecosystem)	3

2.1.1	Truyền hình quảng bá (broadcast TV)	8

2.1.2	Nhà cung cấp truyền hình trả tiền truyền thống (traditional pay-TV operators)	9

2.1.3	Nhà phân phối chương trình video đa kênh (MVPD)	10

2.1.4	TV Everywhere (TVE)	13

2.1.5	Nhà phân phối video trực tuyến (OVD)	14

2.1.6	Đề xuất hiện đại hóa định nghĩa MVPD của FCC	15

2.1.7	Virtual MVPD (vMVPD)	19

2.1.8	Mô hình thuê bao truyền thống	20

2.1.9	Các mô hình thanh toán hiện đại	21

2.1.10	Trả trước (prepaid) vs. trả sau (postpaid)	24

2.1.11	Hệ thống quản lý thuê bao (subscriber management system – SMS)	26

2.2	Truyền phát video trực tuyến (video streaming)	27

2.2.1	Quy trình xử lý nội dung (content workflow)	28

2.2.2	Sản xuất nội dung (video production)	29

2.2.3	Quá trình phân phối (video delivery pipeline)	31

2.3	Thuật ngữ và khái niệm cơ bản (glossary of terms and essential concepts)	34

2.3.1	Bitrate	34

2.3.2	Mezzanine (files)	34

2.3.3	Codecs	35

2.3.4	Containers (format)	36

2.3.5	Encoding	37

2.3.6	Transcoding	38

2.3.7	Muxing (multiplexing)	38

2.3.8	Demuxing (demultiplexing)	39

2.3.9	I-frame (video)	39

2.3.10	Group of Pictures (GOP) size	40

2.3.11	Timecode	41

2.3.12	Renditions	41

2.3.13	Streaming	42

2.3.14	Adaptive bitrate (ABR) streaming	43

2.3.15	Progressive download	43

2.3.16	Adaptive streaming protocols	44

2.3.17	Bitrate ladder	47

2.3.18	Chunk hay chunking	48

2.3.19	Fragmented MP4 (fMP4)	49

2.3.20	CMAF (container)	53

2.3.21	Common Encryption (CENC)	53

2.3.22	Encrypted Media Extensions (EME)	53

2.3.23	Manifest	53

2.3.24	Subtitles và closed captions	53

2.3.25	Thumbnail preview (feature)	56

2.3.26	Chapter markers & cues/cue points	58

2.3.27	Live caption và live transcript	60

2.3.28	Time-shiting (features)	60

2.3.29	In-stream ads	62

2.3.30	In-band events (ads)	62

2.3.31	Ad replacement & ad insertion (ads)	63

2.3.32	Ad stitching (ads)	64

2.3.33	SCTE-35 markers/tags	65

2.3.34	SSAI & DAI	67

3.	ĐẶC TẢ CHUNG (GENERAL SPECIFICATIONS)	69

3.1	Định danh và cấu hình codec (codec identifiers)	69

3.2	Mezzanine transcoding	73

3.3	Codec được hỗ trợ (supported output codecs)	73

3.3.1	Video codecs	73

3.3.2	Tính tương thích của video codecs	75

3.3.3	HDR video formats	77

3.3.4	Audio codecs	79

3.3.5	Tính tương thích âm thanh (audio compatibility)	80

3.4	Container formats	80

3.4.1	Định dạng luồng âm thanh cơ bản (elementary audio stream formats)	80

3.4.2	Tương thích codecs và containers	81

3.5	Tính năng âm thanh Dolby (Dolby audio features)	84

3.5.1	Hỗ trợ Dolby Atmos (Dolby Atmos support)	84

3.5.2	Hỗ trợ Dolby Digital Plus	84

3.6	Nội dung video HDR (HDR video content)	84

3.6.1	Hỗ trợ Dolby Vision (Dolby Vision support)	85

3.7	Giao thức streaming và DRM (streaming protocols & DRM)	85

3.8	Giao thức cast (cast protocols)	88

3.9	Tính năng thumbnail preview (feature)	88

3.10	Tính năng chapter markers & cue points	93

4.	ÂM THANH VÀ PHỤ ĐỀ	94

4.1	Thẻ ngôn ngữ (language tags)	94

4.2	Tên track (track names)	96

4.2.1	Track âm thanh gốc	97

4.2.2	Quy tắc đặt tên	99

4.3	Hỗ trợ nhiều kênh âm thanh (multiple audio tracks support)	104

4.3.1	Thứ tự (hiển thị) audio tracks (audio tracks display order)	107

4.3.2	Hiển thị danh sách audio tracks (player)	110

4.3.3	Cấu hình manifest	111

4.4	Hỗ trợ phụ đề (subtitles & captions support)	113

4.4.1	Thứ tự (hiển thị) phụ đề (subtitles display order)	114

4.4.2	Hiển thị danh sách phụ đề (player)	114

4.4.3	Cấu hình manifest	115

4.5	Cơ chế chọn lựa và fallback (track selection and fallback mechanism)	115

4.5.1	Cơ chế lựa chọn âm thanh/phụ đề	115

4.5.2	Cơ chế dự phòng (fallback)	116

5.	TỔ CHỨC CHUNG CỦA MANIFEST	117

5.1	Tổ chức rendition (rendition structuring)	117

5.2	Nhận diện thiết bị và lựa chọn playlist/manifest	117

6.	ON-DEMAND STREAMING (VOD)	120

7.	LIVE STREAMING	121

8.	DRM & BẢO VỆ NỘI DUNG (DRM & CONTENT PROTECTION)	122

8.1	Device content protection capabilities	122

THAM KHẢO (REFERENCES)	123

APPENDIX — CONFORMANCE REQUIREMENTS/NOTATION	124

DANH MỤC TỪ VIẾT TẮT (ABBREVIATIONS)

DANH MỤC HÌNH ẢNH (LIST OF FIGURES)

Page

Figure 2-1: Biểu đồ khái niệm truyền hình truyền thống (concept map)	4

Figure 2-2: Business Process Framework (eTOM) – Level 0	27

Figure 2-3: Video streaming — Content flow	29

Figure 2-4: Video workflow — Các bước chính tiêu biểu của post-production	30

Figure 2-5: Video platform kết hợp IPTV (non-streaming) và (online) streaming	33

Figure 2-6: Chapter markers với title render trên UI (video canvas) — THEOplayer	58

Figure 2-7: Sử dụng chapter markers cho playlist — YouTube	59

Figure 2-8: Ad replacement vs. ad insertion	63

Figure 2-9: Ad replacement with live streaming	64

Figure 3-1: Hỗ trợ công nghệ HDR	74

Figure 4-1: Minh họa UI của tool thực hiện transcode (multiple audio tracks)	104

Figure 4-2: Cơ chế lựa chọn audio/subtitle	116

Figure 5-1: Cơ chế lựa chọn playlist/manifest dựa trên thông tin thiết bị	119

DANH MỤC BẢNG BIỂU (LIST OF TABLES)

Page

Table 2-1: Các mô hình thanh toán cơ bản	23

Table 2-1: Đặc điểm của Access pass	24

Table 2-1: Khác biệt giữa sản xuất hậu kỳ và sản xuất trực tiếp	31

Table 2-2: Ví dụ yêu cầu về bitrate của video chưa nén (raw video data)	35

Table 2-3: Ví dụ bitrate ladder	48

Table 3-1: Danh sách các video codecs thông dụng	71

Table 3-2: Danh sách các audio codecs thông dụng	72

Table 3-3: Danh sách codec cơ sở (codec base type) thông dụng	73

Table 3-4: Video codecs (đầu ra) được hỗ trợ	74

Table 3-5: Thông số và tính năng cơ bản của output video codec	75

Table 3-6: Devices & video codecs compatibility	77

Table 3-7: Các công nghệ HDR được hỗ trợ	78

Table 3-8: Audio codecs (đầu ra) được hỗ trợ	79

Table 3-9: Tương thích containers và codecs	83

Table 3-10: SUPPLEMENTAL-CODECS và backward-compatibility	85

Table 3-11: Tương thích streaming protocols và DRM	86

Table 3-12: Tương thích giao thức streaming và thiết bị/OS/browser	88

Table 3-13: Thiết lập tần số thời gian khi tạo thumbnails sprites	89

Table 4-1: Ví dụ về cách xác định ngôn ngữ và chữ viết	96

Table 4-2: Ví dụ một số trường hợp tên track hay gặp	103

Table 4-3: Folder/segment name dùng cho URI tương ứng codec identifier	106

Table 5-1: Tổ chức renditions cho VOD	117

GIỚI THIỆU (INTRODUCTION)

Phạm vi và mục tiêu chính

Phạm vi của tài liệu này bao gồm các hướng dẫn chung (general guidelines), các đề xuất thực hiện thực tiễn (best practices) và ví dụ (examples) về việc tổ chức xây dựng và triển khai hệ thống streaming video dựa trên các tiêu chuẩn như HTTP Live Streaming (HLS) và DASH (tức MPEG-DASH).

Tài liệu cung cấp các ví dụ chi tiết về tổ chức manifest, cách chọn và chuyển đổi chất lượng video (rendition switching), cơ chế dự phòng (fallback mechanisms), cũng như các hướng dẫn mã hóa để tối ưu hóa chất lượng và hiệu suất streaming. Ngoài ra, nó còn bao gồm các ví dụ về triển khai từ các nhà cung cấp và hệ thống khác nhau để cung cấp cái nhìn tổng quan về cách thực hiện tốt nhất trong thực tế.

Ký hiệu tuân thủ (conformance requirements/notation)

Trong suốt tài liệu này, các từ được sử dụng để định nghĩa tầm quan trọng của các yêu cầu cụ thể được viết hoa. (Throughout this document, the words that are used to define the significance of particular requirements are capitalized)

Các từ khóa "PHẢI (MUST)", "KHÔNG ĐƯỢC (MUST NOT)", "BẮT BUỘC (REQUIRED)", "SẼ PHẢI (SHALL)", "SẼ KHÔNG ĐƯỢC (SHALL NOT)", "NÊN (SHOULD)", "KHÔNG NÊN (SHOULD NOT)", "KHUYẾN NGHỊ (RECOMMENDED)", "CÓ THỂ (MAY)", và "TÙY CHỌN (OPTIONAL)" trong tài liệu này được hiểu như được mô tả trong RFC 2119.

(The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119)

Xem chi tiết tại “Phụ lục Ký hiệu tuân thủ”

Tiêu chuẩn tham chiếu (reference standards)

Các định nghĩa, thuật ngữ trong các tài liệu/tiêu chuẩn tương ứng sau đây sẽ trở thành các định nghĩa, thuật ngữ trong tài liệu này.

Đối với bất kỳ tài liệu tham khảo nào (any referenced documents) có phiên bản được chỉ định rõ ràng, nội dung hoặc phiên bản sửa đổi, nếu có, sẽ không áp dụng cho tài liệu này. Tuy nhiên, nên xem xét và nghiên cứu để sử dụng phiên bản mới nhất của các tài liệu tham khảo.

Đối với bất kỳ tài liệu tham khảo nào không có phiên bản được chỉ định rõ ràng, các phiên bản mới nhất sẽ áp dụng trong tài liệu này.

Các tiêu chuẩn tham chiếu chính:

Ngoài các tiêu chuẩn tham chiếu chính, các tiêu chuẩn và tài liệu tham khảo còn lại được liệt kê trong phần “THAM KHẢO (REFERENCES)”.

TỔNG QUAN VỀ STREAMING

Hệ sinh thái truyền hình (TV ecosystem)

Về cơ bản, nội dung sẽ từ bên sản xuất, sáng tạo nội dung (content producers/content creators) qua các kênh phân phối hay các nhà phân phối (distributors), tới bên tiêu thụ nội dung (consumers) tức người xem.

Tùy thuộc các thức phân phối mạng lưới này sẽ có độ phức tạp hay các bên tham gia khác nhau.

Phân phối trực tiếp (direct channel) — Đơn giản chỉ đi thẳng từ content producer › consumer

Kênh bán lẻ (retail channel) — Từ content producer › retailer › tới consumer

Có kênh bán buôn/bán sỉ (wholesale channel) — Từ content producer › wholesaler hay distributor › retailer › consumer

Qua kênh đại lý (đại diện, agent channel) — Từ content producer › agent/broker › wholesaler/distributor › retailer › consumer

Việc phân phối nội dung (distribution) được thực hiện thông qua nhiều cách khác nhau, chủ yếu được chia thành truyền hình truyền thống (traditional television), streaming và các phương thức khác.

Truyền hình truyền thống (traditional television) là phương thức phân phối tồn tại trước khi streaming xuất hiện, bao gồm:

Mạng phát sóng (broadcast networks) — Nội dung được phát qua sóng vô tuyến (over-the-air television with radio frequencies). Tín hiệu phát sóng loại này này còn gọi là tín hiệu mặt đất (terrestrial signals) và người dùng cần antenna hay thiết bị nhận tín hiệu (receiver).

Khái niệm mạng phát sóng thể hiện đây là một tổ chức hoặc công ty lớn điều hành nhiều đơn vị nhỏ hơn.

Các công ty và tổ chức thực hiện phát sóng (tín hiệu mặt đất) có thể gọi chung là đài (phát sóng) truyền hình (broadcaster). Một mạng phát sóng thường sẽ bao gồm nhiều đài truyền hình hoạt động ở các khu vực khác nhau.

Các đài truyền hình sẽ sở hữu nhiều trạm phát sóng (television station). Do đó, các đài truyền hình còn được gọi là broadcast television station.

Truyền hình qua mạng lưới cáp (cable networks) — Hệ thống phân phối truyền hình sử dụng cáp, ví dụ cáp đồng trục hay cáp quang (tức hữu tuyến thay vì vô tuyến như mạng phát sóng).

Truyền hình vệ tinh (satellite television) — Phát sóng nội dung truyền hình qua vệ tinh thay vì qua mạng phát sóng (mặt đất) hoặc cáp. Người dùng cần một chảo vệ tinh (satellite dish) để thu tín hiệu từ vệ tinh, kết nối với bộ thu tín hiệu (receiver) chuyển đổi tín hiệu vệ tinh thành tín hiệu truyền hình.

Nền tảng streaming (streaming platforms) tức phân phối thông qua các dịch vụ truyền phát nội dung (streaming) qua Internet.

Khác với các phương thức truyền thống, streaming chỉ cần có kết nối Internet và không phụ thuộc quá nhiều vào loại hạ tầng mạng (network infrastructure) bên dưới.

Các nhà cung cấp dịch vụ Internet (ISP) có thể dùng các công nghệ khác nhau như cáp quang, vệ tinh, hay mạng di động.

Ngoài ra còn có những phương thức khác ví dụ tải về nội dung để xem (download), hay qua các phương tiện vật lý như đĩa DVD. Tạm thời không cần đề cập tới các loại này.

Figure 2-1: Biểu đồ khái niệm truyền hình truyền thống (concept map)

Tại Việt Nam, phân loại dịch vụ truyền hình được quy định trong Điều 4, Nghị định 06/2016/NĐ-CP và bổ sung trong Nghị định 71/2022/NĐ-CP (2022-10) bao gồm:

Truyền hình mặt đất định nghĩa là “truyền hình sử dụng hạ tầng kỹ thuật truyền dẫn phát sóng truyền hình mặt đất kỹ thuật số” hay còn gọi là truyền hình kỹ thuật số mặt đất (Digital Terrestrial Television – DTT)

Truyền hình cáp chia ra làm 3 loại là analog, digital và cả truyền hình cáp giao thức Internet (IPTV). Mặc dù IPTV có thể mở rộng cho cả vệ tinh nhưng hầu hết là qua các mạng băng rộng (broadband) như cáp quang (FTTH).

Truyền hình qua vệ tinh là “truyền hình sử dụng hạ tầng kỹ thuật truyền dẫn phát sóng truyền hình qua vệ tinh” tức là truyền hình kỹ thuật số vệ tinh (Direct to Home – DTH)

Truyền hình di động định nghĩa là truyền hình thông qua mạng viễn thông di động hoặc vệ tinh. Mặc dù có sử dụng vệ tinh, nhưng thiết bị nhắm tới là thiết bị di động như điện thoại di động, máy tính bảng khác với truyền hình qua vệ tinh (điểm c). Truyền hình vệ tinh phát nội dung đến thiết bị cố định tức đầu thu vệ tinh/chảo vệ tinh (satellite dish) kết nối với bộ thu tín hiệu.

Truyền hình trên mạng Internet được định nghĩa là truyền hình sử dụng kết nối mạng Internet thông qua các địa chỉ tên miền của trang thông tin điện tử hoặc các địa chỉ Internet xác định, và bao gồm cả ứng dụng Internet (bổ sung trong Nghị định 71/2022/NĐ-CP).

DTT có thể sử dụng nhiều chuẩn kỹ thuật khác nhau như DVB-T, DVB-T2, ATSC (Hoa Kỳ), ISDB-T (Nhật Bản), hoặc DTMB (Trung Quốc), tùy thuộc vào quốc gia hoặc khu vực. Việt Nam sử dụng DVB-T2 (phiên bản thứ 2 nâng cấp của DVB-T) để thực hiện số hóa truyền hình. Tương tự, truyền hình cáp tại VN như VTVCab, SCTV sử dụng tiêu chuẩn DVB-C.

Như vậy, điểm d, Nghị định 71/2022/NĐ-CP (truyền hình trên mạng Internet) ý muốn chỉ loại hình streaming với web hay apps còn gọi là dịch vụ truyền hình OTT (Over-The-Top). Dịch vụ OTT (media) được định nghĩa:

Là dịch vụ truyền tải nội dung qua Internet công cộng (public Internet)

Người dùng chỉ cần kết nối Internet từ bất kỳ nhà cung cấp nào (từ bất kỳ ISP nào).

Tách biệt việc cung cấp nội dung với đường truyền tức nhà cung cấp dịch vụ OTT độc lập với ISP (ở đây là đường truyền Internet).

Khác với các nhà cung cấp truyền hình truyền thống như over-the-air, cáp hay vệ tinh.

Thị trường truyền hình trả tiền ở Hoa Kỳ là một ví dụ điển hình về hệ sinh thái nhiều thành phần. Đây là một thị trường đa dạng, với lịch sử phát triển đầy đủ qua nhiều giai đoạn. Hơn nữa, Hoa Kỳ đã áp dụng nhiều quy định pháp lý để điều chỉnh hoạt động của ngành. Do đó, thị trường này được dùng để tham khảo.

Các thành phần chính trong hệ sinh thái này bao gồm:

Đầu tiên là hạ tầng mạng (network infrastructure) và Internet được cung cấp bởi các công ty viễn thông (telco) và nhà cung cấp dịch vụ Internet (ISP) như AT&T, Verizon và Comcast.

Telco (telecommunications company, công ty viễn thông) là các công ty cung cấp dịch vụ viễn thông tức dịch vụ thoại (telephony, voice) và truyền thông thông tin (tức gửi/nhận dữ liệu) nói chung.

Ba dịch vụ phổ biến nhất được gọi là "triple play," bao gồm điện thoại (cố định hay di động), dịch vụ Internet băng rộng (broadband) và truyền hình.

Điều này có nghĩa hầu hết các công ty viễn thông lớn đều cung cấp dịch vụ Internet và cũng đóng vai trò là các ISP.

Tất nhiên, cũng có những telco chỉ cung cấp dịch vụ thoại mà không cung cấp Internet hay truyền hình.

Nhờ sở hữu hạ tầng viễn thông có sẵn, tùy thuộc vào loại hạ tầng, các telco thường cung cấp dịch vụ truyền hình cáp hoặc truyền hình IPTV.

Ví dụ, dịch vụ U-verse TV (IPTV) của AT&T (DirecTV).

Hay dịch vụ Xfinity TV (cable TV) của Comcast.

Các nhà cung cấp dịch vụ truyền hình truyền thống (traditional television providers) bao gồm truyền hình cáp và vệ tinh

Sử dụng các hạ tầng vật lý như cáp, vệ tinh hoặc mạng chuyên dụng để truyền tải tín hiệu truyền hình.

IPTV cũng được xếp và dịch vụ truyền hình truyền thống.

Dịch vụ truyền hình cáp (cable networks) có thể kể như Spectrum (Charter Communications), Cox Communications.

Dịch vụ truyền hình vệ tinh (satellite providers) có thể kể như Dish Network.

Các nhà cung cấp nội dung và chương trình (content providers) đóng vai trò quan trọng trong ngành. Họ có thể là các nhà sản xuất nội dung (content producers) hoặc các mạng lưới truyền hình (television networks)

Nhà sản xuất nội dung (content producers) là đơn vị trực tiếp sản xuất ra các chương trình, phim, nhạc …  tức tạo ra nội dung gốc

Nhà sản xuất thường nắm giữ bản quyền đối với nội dung họ tạo ra.

Có thể là các hãng phim (production companies), studio độc lập, hoặc cả các nhà sáng tạo cá nhân.

Mạng lưới truyền hình (television networks) đóng vai trò trung gian, kết nối nhà sản xuất và khán giả.

Có thể bao gồm nhiều nhà đài (broadcasters), kênh truyền hình (television channels), hoặc nền tảng liên kết được với nhau.

Thường mua bản quyền từ các nhà sản xuất để phát sóng nhưng cũng có thể tự sản xuất nội dung.

Mạng lưới truyền hình chủ yếu thực hiện phân phối nội dung, đóng vai trò “bán buôn” trong khi các nhà cung cấp dịch vụ truyền hình đóng vai trò “bán lẻ”.

Walt Disney Studios, Warner Bros., Paramount Pictures, Universal Pictures, Sony Pictures là những ví dụ điển hình các hãng phim lớn (major production companies).

ABC (American Broadcasting Company), CBS (Columbia Broadcasting System), Fox, và NBC (National Broadcasting Company) là ví dụ cho những mạng lưới truyền thông lớn (major television networks) ở cấp độ quốc gia (tại Hoa Kỳ). Hiệp hội của 4 mạng lưới truyền hình này gọi là Four Affiliates Associations.

CNN, ESPN, HBO, Discovery Channel hay Cartoon Network là ví dụ cho kênh truyền hình chuyên biệt.

CNN chuyên về tin tức và thông tin (news).

ESPN nổi bật với nội dung thể thao (sports).

HBO chuyên về phim (movies) và giải trí (entertainment), đặc biệt là các series gốc (original series).

Discovery Channel chuyên về nội dung khám phá (exploration), khoa học (science), và tự nhiên (nature).

Cartoon Network là kênh chuyên hoạt hình (animation) và giải trí cho trẻ em (kids).

Các dịch vụ streaming trực tuyến (streaming services) như Netflix, Hulu, Disney+, Max, Amazon Prime

Chủ yếu cung cấp nội dung theo yêu cầu (video on demand – VOD), có thể xem bất cứ lúc nào, tùy theo nhu cầu mà không phụ thuộc vào lịch phát sóng. Do đó còn được gọi là dịch vụ streaming theo yêu cầu (on-demand streaming services)

Không cung cấp nội dung là kênh truyền hình.

Các dịch vụ truyền hình trực tiếp (live TV streaming services) như YouTube TV, Hulu + Live TV, và Sling TV

Ngoài VOD các dịch vụ này còn phát sóng trực tiếp các chương trình truyền hình giống như truyền hình truyền thống.

Nội dung truyền hình trực tiếp là các kênh thông thường như của ABC, NBC, CBS, Fox.

Khác biệt chính giữa streaming và live TV streaming là live TV streaming có thêm các kênh truyền hình, ví dụ:

YouTube TV so với YouTube thông thường

Hay Hulu + Live TV so với Hulu (không có truyền hình).

Truyền hình quảng bá (broadcast TV)

Truyền hình quảng bá (broadcast TV) là một hình thức phân phối nội dung truyền hình trực tiếp đến khán giả thông qua sóng vô tuyến (over-the-air), thường không yêu cầu người xem phải trả phí để xem. Người tiêu dùng không cần đăng ký các dịch vụ truyền hình trả tiền (như cáp hoặc vệ tinh) mà chỉ cần sở hữu TV (television sets) có khả năng thu tín hiệu OTA (over-the-air). Hệ thống này cho phép người xem tiếp cận nhiều loại chương trình khác nhau, bao gồm tin tức, thể thao, giải trí và các chương trình địa phương. Nội dung của các đài truyền hình cũng là nguồn cung cấp nội dung (input) cho các dịch vụ truyền hình trả tiền.

Hai nhóm khách hàng của các đài (phát sóng) truyền hình:

Khán giả/người xem (audiences) — Các đài truyền hình phải cố gắng tạo nội dung hấp dẫn để thu hút người xem.

Nhà quảng cáo (advertisers) — Doanh thu chủ yếu của đài truyền hình đến từ quảng cáo. Mức giá phụ thuộc vào quy mô và đặc điểm nhân khẩu học (demographics).

Các đài phi thương mại (non-commercial broadcasters) không dựa vào doanh thu quảng cáo nhưng có thể kiếm doanh thu từ các nguồn khác như tài trợ, quyên góp (donations), hay các chương trình gây quỹ (fundraising drives).

Broadcast TV nói chung có thể kiếm lợi nhuận qua nhiều hình thức:

Quảng cáo (advertising) — Đây là nguồn thu rất lớn cho broadcast TV. Những khung giờ có lượng người xem cao như “prime time” (từ 8-11 giờ tối) thường có giá quảng cáo đắt nhất.

Phí tiếp sóng/tái phát sóng (retransmission fees) — Thu từ các công ty cung cấp dịch vụ truyền hình cáp, vệ tinh và IPTV (các traditional pay-TV operators) để được quyền phân phối kênh.

Bản quyền nội dung (licensing & syndication) — Bán bản quyền phát sóng cho các chương trình hoặc phim mà họ sản xuất hoặc sở hữu. Syndication là thuật ngữ chỉ việc bán lại các chương trình cũ thường cho các đài truyền hình địa phương hoặc các nền tảng streaming.

Tài trợ chương trình (program sponsorship) — Nhận tiền tài trợ từ các doanh nghiệp trả tiền để tài trợ cho một chương trình cụ thể, và đổi lại tên thương hiệu của họ sẽ được xuất hiện trong chương trình hoặc có các quảng cáo liên quan (coi như một hình thức quảng cáo đặc biệt).

Tiền bản quyền từ nội dung số (digital rights & streaming) — Bán hoặc cấp quyền truy cập nội dung cho các nền tảng streaming hoặc kiếm lợi nhuận thông qua nền tảng streaming riêng.

Đây là hình thức cấp quyền để phân phối lại nội dung, tương tự như bản quyền nội dung (licensing & syndication)

Sự khác biệt nằm ở chỗ nội dung với bản quyền nội dung số (digital rights) sẽ phân phối thông qua streaming trong khi đó nội dung với bản quyền nội dung phải sử dụng hình thức phân phối kiểu truyền hình truyền thống (phát sóng theo lịch).

Các sản phẩm liên quan (merchandising) — Đối với các chương trình nổi tiếng, đài truyền hình có thể kiếm tiền từ việc bán các sản phẩm liên quan đến chương trình, như quần áo, đồ chơi, hoặc sách, thường là các sản phẩm có thương hiệu (branded merchandise).

Nhà cung cấp truyền hình trả tiền truyền thống (traditional pay-TV operators)

Dịch vụ truyền hình được định nghĩa là dịch vụ ứng dụng viễn thông

Việc gửi và nhận nội dung hoặc tín hiệu truyền hình thực chất là gửi, nhận và xử lý thông tin, phù hợp với định nghĩa về dịch vụ viễn thông.

Do vậy các nhà cung cấp dịch vụ phải sở hữu hạ tầng mạng viễn thông hoặc phải thuê hạ tầng mạng viễn thông của một bên khác.

Như đã nói, hầu hết các telco cũng là nhà cung cấp dịch vụ truyền hình truyền thống nhờ sở hữu hạ tầng có sẵn.

Với việc sử dụng hạ tầng viễn thông và các vấn đề liên quan đến thiết bị (tức thiết bị tại nhà khách hàng Customer Premise Equipment – CPE), chi phí và pháp lý khiến hầu hết dịch vụ truyền hình áp dụng mô hình trả tiền như telco. Vì vậy, các nhà cung cấp dịch vụ truyền hình truyền thống còn được gọi là các nhà cung cấp truyền hình trả tiền truyền thống (traditional pay-TV operators).

Về mặt kỹ thuật pay-TV có thể triển khai qua DTT platform, tuy nhiên, điều này không phổ biến trong thực tế.

PC Magazine định nghĩa pay-TV được là “dịch vụ thuê bao truyền hình cung cấp bởi các công ty cáp, vệ tinh hoặc viễn thông và loại trừ các dịch vụ Internet-based streaming services như Netflix, Hulu”. Vì vậy, dù Netflix, Hulu cũng tính phí hàng tháng nhưng chúng không được xếp vào nhóm “pay-TV”.

A subscription to a television service from a cable, satellite or telephone company. The term pay TV generally excludes Internet-based streaming services such as Netflix and Hulu, which also charge a monthly fee. Although streaming fees are much lower than a pay TV package, the fees add up if viewers subscribe to several streaming channels. — Definition of pay TV | PCMag

Mặt khác, cần lưu ý rằng Nghị định 71/2022/NĐ-CP (2022-10) định nghĩa truyền hình trả tiền (tức “pay-TV” trong tiếng Việt) có bao gồm dịch vụ qua Internet (streaming).

Điều này cho thấy sự thay đổi trong cách hiểu về "truyền hình trả tiền”, không còn giới hạn ở các mô hình truyền thống như trước đây.

Khi đề cập đến khái niệm pay-TV, nên thêm cụm từ “truyền thống” khi muốn làm rõ nó không bao gồm các dịch vụ streaming dựa trên Internet.

Tham khảo thêm

Pay television - Wikipedia

Các phần tiếp theo sẽ tiếp tục phân tích chi tiết hơn về việc phân loại các dịch vụ truyền hình.

Nhà phân phối chương trình video đa kênh (MVPD)

Các khái niệm như broadcast TV, pay-TV “truyền thống”, và OTT/Internet-based streaming thường được sử dụng để mô tả các dịch vụ hay phương thức phân phối nội dung video. Tuy nhiên, đây chỉ là các thuật ngữ thông dụng trong ngành, thường không phải là định nghĩa pháp lý chính thức.

Ở Hoa Kỳ, các định nghĩa pháp lý về các phương thức phát sóng và cung cấp nội dung truyền hình phải tuân theo Đạo luật Truyền thông (Communications Act), các quy định của Ủy ban Truyền thông Liên bang (Hoa Kỳ) (Federal Communications Commission – FCC), và các luật liên quan đến viễn thông.

Ví dụ, “nhà phân phối chương trình video đa kênh” (tạm dịch cho Multichannel Video Programming Distributor – MVPD) là một khái niệm pháp lý đã được xác định rõ. Trong khi đó OTT vẫn đang còn được tranh luận về việc có nên được điều chỉnh dưới cùng một khuôn khổ hay không.

MVPD được định nghĩa (theo U.S. Code under Title 47, Section 522) như sau:

Một thực thể cung cấp nhiều kênh (multichannel) đến các thuê bao với nội dung kênh là các “chương trình video” (video programming).

“Chương trình video” (video programming) được định nghĩa là chương trình (nội dung) được cung cấp bởi các trạm phát sóng truyền hình (television broadcast station), hoặc nội dung tương tự (theo Section 522 (20)).

Video programming có thể là chương trình trực tiếp (live programming), chương trình gần trực tiếp (near-live programming, ghi hình ít hơn 24 giờ trước thời điểm phát sóng lần đầu tiên), hay chương trình được ghi hình trước (prerecorded programming, không phải "trực tiếp" hoặc "gần trực tiếp")

Nói một cách đơn giản, nó chính là nội dung của các kênh truyền hình.

Thuật ngữ này bao gồm cả phim (hay on-demand video nói chung) và truyền hình.

Nội dung phim hay on-demand video là một loại prerecorded programming

Trong khi đó truyền hình trực tiếp (live video) có thể được phân loại là (can be

classified as) live programming hoặc near-live programming.

Có nghĩa, MVPD sở hữu hay vận hành hệ thống phân phối truyền hình trả tiền (không phải hệ thống mở), “bao gồm nhưng không giới hạn”:

Hệ thống truyền hình cáp.

Hệ thống BRS/EBS (Broadband Radio Service/Educational Broadband Service) tức qua sóng vô tuyến.

Hệ thống vệ tinh phát sóng (quảng bá) trực tiếp (Direct Broadcast Satellite – DBS).

Hay các hệ thống vệ tinh trực tiếp (tới nhà/tại nhà) (Direct to Home – DTH), còn gọi là “truyền hình số vệ tinh”.

“Multichannel video programming distributor. A person such as, but not limited to, a cable operator, a BRS/EBS provider, a direct broadcast satellite service, or a television receive-only satellite program distributor, who owns or operates a multichannel video programming system.” (47 CFR § 76.1200 (cornell.edu))

MVPD sẽ tương đương với khái niệm nhà cung cấp dịch vụ truyền hình trả tiền truyền thống (traditional pay-TV operator). MVPD có quyền cung cấp các kênh truyền hình (linear channels) thông qua các hợp đồng cấp phép (licensing access) từ các đài truyền hình (broadcasters) và các đơn vị truyền hình cáp (cable companies).

Tất nhiên, ngoài quyền lợi, MVPD phải tuân thủ các yêu cầu và quy định nghiêm ngặt:

Must-carry — Quy định yêu cầu các MVPD, cụ thể là các hệ thống truyền hình cáp, phải tiếp phát sóng các đài truyền hình địa phương (local stations) có lượng người xem đáng kể (significantly viewed).

Có nghĩa kênh của các đài truyền hình này phải được đưa vào danh sách kênh của nhà cung cấp dịch vụ để đảm bảo người xem có thể tiếp cận các chương trình địa phương.

Nó cũng giúp bảo vệ các đài truyền hình địa phương khỏi bị loại trừ khỏi các hệ thống truyền hình trả tiền và mất đi lượng khán giả.

Tương tự, VTV1 là một trong 7 kênh truyền hình thiết yếu quốc gia của Việt Nam (must-carry national channels).

Yêu cầu must-carry sẽ đi kèm với quy định về quyền tiếp sóng (retransmission consent)

Ngược lại với must-carry, retransmission consent cho phép đài truyền hình có quyền không cho MVPD tiếp sóng. Đây cũng là cơ sở để các đài truyền hình yêu cầu MVPD trả phí tiếp sóng.

Đài truyền hình ba năm một lần có quyền lựa chọn giữa must-carry (không nhận tiền, without receiving compensation) hay retransmission consent (đàm phán để đạt một thỏa thuận tiếp sóng).

Nếu các đài truyền hình chọn retransmission consent thì MVPD sẽ không còn nghĩa vụ (no obligation) phải tiếp sóng (xem thêm Retransmission Consent | FCC)

Kênh truy cập công cộng (public access channels) — Là yêu cầu về các kênh truyền hình không vì lợi nhuận, cung cấp cho công chúng quyền được tạo và phát sóng nội dung.

Các kênh truy cập công cộng hay còn gọi là PEG channels chia thành ba loại

Kênh truy cập công cộng (public access channels) dành cho công chúng hoặc các tổ chức phi lợi nhuận.

Kênh giáo dục (educational access channels) phát sóng các chương trình giáo dục từ các trường học, cao đẳng, đại học, và các tổ chức học thuật.

Kênh chính phủ (government access channels) phát sóng các chương trình liên quan đến hoạt động chính phủ, cuộc họp công khai, và các vấn đề công dân.

Các kênh này có thể được quản lý bởi MVPD hoặc một bên thứ ba do cơ quan quản lý có thẩm quyền chỉ định (designated by the franchising authority) hoặc trực tiếp bởi chính quyền địa phương (local governments) như trong trường hợp là kênh chính phủ.

Những kênh này đóng vai trò bảo đảm quyền tự do ngôn luận, đảm bảo môi trường truyền thông tự do, và cung cấp các nội dung không vì lợi nhuận dành cho cộng đồng.

Ngoài ra còn những quy định khác, ví dụ như:

Cung cấp thông tin dịch vụ khẩn cấp (emergency service information) như cảnh báo thiên tai, lũ lụt và thông tin trong các tình huống khẩn cấp quốc gia.

Phải tuân thủ các quy định về cung cấp dịch vụ cho người khuyết tật, bao gồm việc cung cấp phụ đề (closed captioning), dịch vụ truyền hình cho người khiếm thị/khiếm thính, và các tính năng hỗ trợ khác.

MVPD còn phải cung cấp thông tin và báo cáo định kỳ cho các cơ quan quản lý, bao gồm số lượng thuê bao, nội dung phát sóng, và các vấn đề liên quan đến tuân thủ quy định.

Tuân thủ các quy định về thiết bị (navigation devices), hạ tầng, cung cấp thông tin rõ ràng về các dịch vụ của họ, bao gồm giá cả, điều khoản hợp đồng và các chính sách hủy dịch vụ.

Xem thêm

Multichannel television in the United States - Wikipedia

Trước khi FCC thông qua “Thông báo Đề xuất ban hành quy định” (tạm dịch cho Notice of Proposed Rulemaking – NPRM) vào năm 2014 nhằm mở rộng khái niệm MVPD, các dịch vụ streaming truyền thống như Netflix, Hulu không được phát sóng kênh truyền hình trực tiếp vì họ không được công nhận là MVPD. Sự thay đổi về quy định của FCC đã đánh dấu một bước ngoặt quan trọng, tạo điều kiện cho sự ra đời của các dịch vụ vMVPD (virtual MVPD).

TV Everywhere (TVE)

Năm 2013 đánh dấu sự giảm sút đầu tiên về số lượng thuê bao MVPD tại Hoa Kỳ. Nguyên nhân chủ yếu là do khách hàng chuyển từ dịch vụ MVPD cáp sang các dịch vụ streaming video theo yêu cầu (video on demand) như Netflix. Để đối phó với xu hướng này, các MVPD đã tăng cường triển khai các dịch vụ video tương tự gọi là “TV Everywhere” (TVE).

Xem thêm

TV Everywhere - Wikipedia

TVE cho phép các thuê bao MVPD truy cập cả chương trình truyền hình tuyến tính (tức kênh truyền hình) lẫn video theo yêu cầu (VOD). Người dùng có thể xem trên nhiều thiết bị kết nối Internet, có thể là tại nhà và hay di động miễn được cấp phép bởi MVPD (devices authorized by MVPD).

Hình thức cấp phép thông thường qua chứng thực tài khoản (authentication). Người dùng sẽ đăng nhập vào tài khoản (user ID và password) đã được liên kết với thuê bao MVPD của họ. Điều này cho phép họ truy cập vào các nội dung và dịch vụ mà họ đã trả tiền. Chính vì vậy TVE còn được gọi là “authenticated streaming” và TVE app gọi là “authenticated app” hay “TV Go authenticated app”.

TVE được FCC xem như là sáng kiến của các MVPD (MVPD initiative) dành cho khách hàng thuê bao hiện hữu (trích từ báo cáo lần thứ 14 của FCC về “tình hình cạnh tranh của thị trường truyền hình”, MB Docket No. 07-269, ngày 20 tháng 7 năm 2012).

“TV Everywhere” refers to an MVPD initiative, which allows subscribers of certain services to access video programming on stationary and mobile Internet-connected devices, including television sets, computers, tablets, and smartphones.

Nhà phân phối video trực tuyến (OVD)

FCC định nghĩa “nhà phân phối video trực tuyến” (tạm dịch cho online video distributor – OVD) vào năm 2013 (cũng trích từ báo cáo lần thứ 14) là “bất kỳ thực thể nào cung cấp nội dung video thông qua Internet hoặc con đường truyền (dẫn) dựa trên giao thức Internet (Internet Protocol – IP) do một cá nhân hoặc tổ chức khác cung cấp (tức không phải của chính OVD)”.

An “OVD” is any entity that offers video content by means of the Internet or other Internet Protocol (IP)-based
transmission path provided by a person or entity other than the OVD. An OVD does not include an MVPD inside
its MVPD footprint or an MVPD to the extent it is offering online video content as a component of an MVPD
subscription to customers whose homes are inside its MVPD footprint.

Theo đó, FCC chia các đơn vị truyền tải (delivers) nội dung video thành ba nhóm:

Các nhà phân phối chương trình video đa kênh (MVPD)

Các đài (phát sóng) truyền hình (broadcast television stations)

Các nhà phân phối video trực tuyến (OVD)

Lưu ý:

Trong nhóm này broadcast television stations không được phân loại là nhà cung cấp (providers) mà chỉ là đơn vị truyền tải (delivers) vì không cung cấp dịch vụ thuê bao (subscription service).

Báo cáo lần thứ 14 cũng là lần đầu tiên FCC áp dụng khung phân tích mới, trong đó tách các đài truyền hình (over-the-air) thành một nhóm riêng biệt và tập trung vào phân tích các MVPD. Nó cũng đánh dấu sự thay đổi quan trọng trong cách FCC đánh giá thị trường truyền hình và các dịch vụ video.

OVD và MVPD được định nghĩa là hai thực thể độc lập và có những quy định riêng biệt.

OVD sẽ không bao gồm MVPD trong chính khu vực hoạt động mình (MVPD footprint).

MVPD vẫn có thể cung cấp video qua giao thức IP trong hạ tầng của mình (ví dụ IPTV).

Đường truyền (transmission path) của OVD phải là của một bên khác.

Ngay cả khi MVPD mở rộng, cung cấp dịch vụ trực tuyến (online) cho khách hàng như một phần trong gói thuê bao, nếu thuê bao này vẫn nằm trong hạ tầng của MVPD, thì đó vẫn không được coi là dịch vụ OVD.

Có nghĩa MVPD vẫn chỉ đang cung cấp dịch vụ cho khách hàng thuê bao sử dụng tại nhà nằm trong hạ tầng của MVPD.

Điều này cũng sẽ loại trừ TV Everywhere khỏi định nghĩa OVD.

Đề xuất hiện đại hóa định nghĩa MVPD của FCC

Trong báo cáo lần thứ 14 (tháng 7 năm 2012), FCC đã bắt đầu lưu ý một số MVPD như Comcast, Cox, và AT&T đã cho phép cả những khách hàng không phải đăng ký thuê bao (non-subscribers) truy cập một phần nội dung video trực tuyến thông qua TV Everywhere. Trong khi đó, Time Warner Cable và Verizon vẫn chỉ cho phép khách hàng thuê bao truy cập nội dung thông qua dịch vụ này.

Các báo cáo lần thứ 14, 15 (2013-7) và sau đó là 16 (2015-3), đánh giá rằng:

Chiến lược TVE của MVPD đang tạo áp lực cho các OVD.

Trong báo cáo quý 3 năm 2012, Netflix xác định dịch vụ TV Everywhere là đối thủ cạnh tranh chính.

Đến cuối năm 2013, 85% phim trên TVE của Comcast không có trên Netflix, và 62% không có trên Hulu. Đối với TV shows, tỷ lệ này là 95% không có trên Netflix và 44% không có trên Hulu.

TVE chủ yếu cung cấp VOD nhưng bắt đầu tăng cường nội dung trực tiếp (live content).

TWC TV app cho phép xem 24 kênh, Charter TV App cho phép xem hơn 100 kênh.

TVE của Comcast cho xem online streaming London Olympics 2012 và Sochi Winter Olympics 2014.

Điều này cho thấy MVPD đã mở rộng dịch vụ từ truyền hình theo lịch phát sóng sang trực tuyến.

Xu hướng sử dụng OVD vẫn tiếp tục tăng.

Người dùng thích xem video ở bất kỳ thời gian và địa điểm nào (anywhere & anytime).

Netflix báo cáo doanh thu tăng từ 3.6 tỷ USD năm 2012 lên 4.4 tỷ USD năm 2013.

OVD chiếm một phần ngày càng tăng trong lưu lượng truy cập Internet.

Điều này gây áp lực cho các ISP (thường là MVPD) phải đầu tư nâng cấp hạ tầng.

OVD thường không trả tiền cho việc đầu tư hạ tầng của ISP, gây tranh cãi về phân chia chi phí và trách nhiệm.

Tính không minh bạch của các OVD

Thực tế cho thấy rất khó thống kê số lượng người dùng của OVD

Chỉ có Netflix công bố công khai số liệu về người đăng ký và doanh thu.

Nhiều OVD liên kết với các công ty con hoặc bộ phận của các công ty lớn kinh doanh đa ngành, hay sở hữu tư nhân càng gia tăng tính không minh bạch. Trường hợp được lấy làm ví dụ là Hulu (của Disney).

Các OVD buộc phải cải thiện và mở rộng nội dung để giữ chân và thu hút người dùng. Tuy nhiên việc mở rộng nội dung cũng chỉ giới hạn trong hai cách

Đàm phán để độc quyền nội dung.

Đầu tư vào nội dung gốc.

Những vấn đề này cho thấy sự phức tạp trong việc quản lý các dịch vụ video. Căng thẳng giữa truyền hình truyền thống và các nền tảng mới yêu cầu phải có khuôn khổ quy định để cân bằng lợi ích của tất cả các bên liên quan.

Vào ngày 19 tháng 12 năm 2014, FCC thông qua một NPRM (MB Docket No: 14-261), đưa ra đề xuất “hiện đại hóa định nghĩa MVPD”. Mục tiêu của việc điều chỉnh này là:

Phù hợp với sự thay đổi công nghệ trong ngành phân phối video.

Đáp ứng nhu cầu ngày càng tăng của người tiêu dùng trong việc truy cập nội dung video thông qua các nền tảng khác nhau, bao gồm streaming qua Internet.

Thúc đẩy việc triển khai thêm băng thông rộng (broadband deployment)

Đảm bảo phù hợp với thực tiễn thị trường hiện tại.

Đảm bảo các MVPD truyền thống vẫn phải tuân thủ các quy định khi dịch chuyển dịch vụ sang nền tảng Internet.

Đồng thời tạo điều kiện cho các dịch vụ streaming qua Internet cạnh tranh với các nhà cung cấp truyền thống

Cuối cùng là tạo cơ hội cạnh tranh công bằng cho tất cả các nhà cung cấp dịch vụ.

Cụ thể, hai đề xuất cho định nghĩa MVPD là:

Nhà phân phối nhiều “luồng chương trình video tuyến tính”, bao gồm cả các dịch vụ dựa trên Internet (distributors of multiple linear video programming streams, including Internet-based services).

FCC diễn giải “channels of video programming” có nghĩa là “linear streams of video programming”.

Lý do khái niệm kênh (channels) có thể liên quan đến tần số (và các vấn đề như cấp phép, cũng như luật viễn thông) và hạ tầng truyền dẫn

Linear được hiểu là được lên lịch trước (prescheduled).

Tập trung vào khái niệm “phân phối luồng chương trình video tuyến tính”, bất kể công nghệ truyền tải.

Mở rộng phạm vi của MVPD và gộp chung cả OVD.

Cách thứ hai phản ánh hướng tiếp cận truyền thống, yêu cầu nhà phân phối phải kiểm soát đường truyền để đủ điều kiện là MVPD (distributor to have control over a transmission path to qualify as an MVPD). Điều này sẽ loại trừ các OVD.

Đề xuất đầu tiên được FCC ủng hộ và cho rằng là cách giải thích hợp lý.

Xem chi tiết tại Commission Adopts MVPD Definition NPRM Docket No. 14-261 | FCC (fcc.gov)

Sự thay đổi này cũng liên quan đến vai trò của FCC trong quản lý Internet, ảnh hưởng đến cách thức các nhà cung cấp dịch vụ Internet hoạt động. Trước đây, FCC áp dụng cách tiếp cận rất thận trọng, được gọi là “hands-off the Internet”:

Đây là cách tiếp cận mà các cơ quan quản lý chức năng, như FCC, không can thiệp vào hoạt động của Internet.

Có nghĩa không được đưa ra các quy định nghiêm ngặt hoặc hạn chế lên ISP và các nền tảng trực tuyến.

Cho phép thị trường tự do phát triển và không bị quản lý chặt chẽ từ phía chính phủ.

Mối liên hệ chặt chẽ giữa Internet và các dịch vụ truyền hình cùng khái niệm “trung lập mạng” (net neutrality) đã làm thay đổi điều này:

Khái niệm net neutrality yêu cầu các ISP phải đối xử bình đẳng với tất cả dữ liệu lưu thông, không phân biệt giữa các loại nội dung, ứng dụng, hoặc nguồn gốc của dữ liệu.

ISP không được phép ưu tiên, hạn chế hoặc chặn bất kỳ nội dung hoặc dịch vụ nào trên Internet.

Đáp lại đề xuất của FCC, các nhà cung cấp dịch vụ truyền hình cáp đã phản đối mạnh mẽ MVPD NPRM. National Cable & Telecommunications Association (NCTA), tổ chức đại diện cho ngành công nghiệp cáp và truyền thông tại Hoa Kỳ, cho rằng đường truyền dựa trên cơ sở hạ tầng (facilities-based transmission path) phải là yếu tố thiết yếu để xác định trạng thái (status) của một MVPD, bao gồm cả quyền và nghĩa vụ. Điều này có nghĩa là nó không chỉ đảm bảo khả năng phân phối nội dung mà còn đáp ứng các yêu cầu pháp lý và quy định liên quan đến việc cung cấp dịch vụ truyền hình:

Đảm bảo chất lượng dịch vụ.

Tuân thủ các quy định về quyền truy cập vào nội dung.

Tuân thủ các các nghĩa vụ liên quan khác.

Đề xuất MVPD NPRM đánh dấu giai đoạn lấy ý kiến công khai từ các bên liên quan.

Hiện tại (dù đã 10 năm trôi qua), MVPD NPRM vẫn còn trong quá trình xem xét

Nhiều vấn đề chưa được giải quyết triệt để thông qua quá trình lập pháp.

Dù vậy, một số quy định có thể được áp dụng tạm thời trong khi chờ quy trình hoàn tất.

FCC đã tạm thời kết luận rằng để được coi là MVPD, nhà phân phối phải kiểm soát cả nội dung lẫn đường truyền.

Các OVD không có đường truyền riêng (không sở hữu hoặc điều hành các cơ sở hạ tầng), sẽ không thể kiểm soát các kênh dựa trên hạ tầng (facilities-based channel). Do đó, OVD không thể phân phối nội dung loại này.

Vẫn tách biệt định nghĩa MVPD và OVD

Tuy nhiên, FCC cũng đã quyết định cung cấp cho OVD một con đường khác để trở thành MVPD thông qua hợp tác, marketing hoặc liên doanh (joint venture) với các ISP, MVPD hay broadcaster:

Một thực thể không cần phải sở hữu đường truyền (transmission path) để trở thành MVPD miễn là nó có thể cung cấp một luồng lập trình tuyến tính liên tục được lên lịch trước (continuous linear stream of prescheduled programming).

Tức là thực hiện giống như truyền hình truyền thống nhưng vẫn phân biệt với dịch vụ streaming như Netflix (chủ yếu là on-demand).

Tạo điều kiện cho các nhà cung cấp dịch vụ không sở hữu hạ tầng truyền thống tham gia thị trường.

Virtual MVPD (vMVPD)

Thuật ngữ MVPD “ảo” (virtual MVPD) thường được sử dụng để chỉ các dịch vụ như YouTube TV, Hulu + Live TV và Sling TV

YouTube TV là dịch vụ của Google có hợp tác với các mạng lưới truyền hình lớn như ABC, NBC, CBS, Fox, CW, và PBS.

Hulu + Live TV có cổ đông chính là Disney và Comcast, vốn đã sở hữu các mạng lưới truyền hình lớn như ABC, NBC và các kênh truyền hình phổ biến như ESPN, Disney Channel

Sling TV là công ty con của DISH Network, một nhà cung cấp dịch vụ truyền hình vệ tinh lớn

Các dịch vụ này cung cấp các gói kênh truyền hình trực tuyến qua Internet, tương tự như các gói được cung cấp bởi các nhà cung cấp truyền hình truyền thống. Chúng cũng được gọi là dịch vụ live TV streaming (tức nhấn mạnh có kênh truyền hình) để phân biệt với các dịch vụ streaming như Netflix, chủ yếu chỉ cung cấp video theo yêu cầu (on-demand video).

Như đã nói, MVPD NPRM 2014 của FCC đã mở đường cho các dịch vụ vMVPD.

Thuật ngữ "virtual MVPD" không được định nghĩa rõ ràng trong các văn bản.

Thay vào đó nó được xem là ứng dụng của khái niệm “tương đương về mặt chức năng” (functional equivalency)

Có nghĩa các nhà phân phối thông qua Internet (Internet-based distributors) có quyền lựa chọn trở thành “thực thể giống như MVPD” nếu họ chấp nhận cả quyền lợi lẫn nghĩa vụ liên quan.

For example, some commenters call for a “functional equivalency” standard, whereby an entity would qualify as an MVPD if it looks and functions like a traditional MVPD from the perspective of consumers; others suggest that Internet-based distributors should be allowed to elect whether or not to avail themselves of MVPD status, taking on both the benefits of such status (such as program access) as well as the regulatory obligations. (trích MB Docket No. 14-261)

Dù đã 10 năm trôi qua, vẫn có nhiều phản đối nhất là từ hiệp hội của bốn mạng lưới truyền hình lớn Four Affiliates Associations (tức ABC Television Affiliates Association, CBS Television Network Affiliates Association, FBC Television Association tức Fox và NBC Television Affiliates). Gần đây (2024-03), luật sư của Four Affiliates Associations yêu cầu FCC phải chú ý hơn đến các vMVPDs (tham khảo “Customer Rebates for Undelivered Video Programming During Blackouts”, MB Docket No. 24-20).

Liên quan vấn đề bồi thường cho khách hàng khi bị gián đoạn dịch vụ.

Yêu cầu một khung quy định rõ ràng và công bằng cho cả MVPDs và vMVPDs (truyền hình qua Internet)

Các vMVPDs phải tuân theo các quy tắc tương tự như truyền hình trả tiền truyền thống

Cho rằng các vMVPDs đang hoạt động ngoài khuôn khổ quy định về quyền tiếp sóng (retransmission consent) gây thiệt hại cho các đài truyền hình.

Mô hình thuê bao truyền thống

Quản lý thuê bao/đăng ký (subscriber management) là một quy trình để quản lý khách hàng từ khi họ đăng ký sản phẩm hoặc dịch vụ (subscribe to a product or service) cho đến khi họ hủy đăng ký (cancel the subscription).

Theo định nghĩa truyền thống, thuê bao đăng ký dịch vụ (subscription) được xác định thông qua hợp đồng giữa người mua và người bán, liên quan đến các khoản thanh toán định kỳ cho hàng hóa hoặc dịch vụ. Nói cách khác, mô hình kinh doanh thuê bao (subscription business model) là một mô hình trong đó khách hàng (customer) phải trả tiền định kỳ (recurring payment) theo các khoảng thời gian đều đặn (regular intervals) để truy cập vào sản phẩm hoặc dịch vụ.

A subscription is a contract between a buyer and seller for a recurring payment for a good or service.

Các nhà cung cấp dịch vụ viễn thông (telco) hay dịch vụ truyền hình trả tiền (pay-TV operators) từ lâu đã sử dụng mô hình thuê bao vì người dùng thường sử dụng các dịch vụ này trong thời gian dài. Các khoản thanh toán định kỳ thường là trả sau (postpaid) và được được lên lịch với chu kỳ hóa đơn (billing cycle, recurring billing) hàng tháng hoặc hàng năm (monthly or annually). Do đó, hệ thống quản lý thuê bao (subscriber management system – SMS) từ lâu là một thành phần “truyền thống” và quan trọng trong hệ thống của các công ty telco hay pay-TV.

Các mô hình thanh toán hiện đại

Các dịch vụ hiện nay thường áp dụng các mô hình thanh toán cơ bản khác nhau về cách tính phí và mức độ linh hoạt trong sử dụng.

Thanh toán định kỳ (recurring payment) → nền tảng của mô hình thuê bao (subscription model)

Người dùng thanh toán định kỳ theo chu kỳ cố định (tháng, quý, năm) để duy trì quyền truy cập dịch vụ.

“Recurring” có nghĩa là lặp lại theo chu kỳ đều đặn, không nhất thiết phải tự động gia hạn (auto-renew), nhưng nếu có thì cũng theo lịch trình định sẵn.

Đây là đặc điểm chính để xếp một mô hình thanh toán là subscription business model (theo định nghĩa trên Wikipedia).

Thuê bao định kỳ cố định (fixed recurring subscription)

Khoản thanh toán là cố định, không phụ thuộc vào mức sử dụng (non-volume).

Người dùng xem ít hay nhiều vẫn trả cùng một mức phí trong mỗi chu kỳ.

Là một mô hình kinh doanh cụ thể thường đi kèm các gói tháng, quý, hoặc năm.

Tức là một loại hình cụ thể của recurring payment.

Recurring payment chỉ mới đề cập hình thức hoặc cơ chế thanh toán, trong đó khoản tiền được thu lặp lại theo chu kỳ cố định (tháng, quý, năm...).

Ví dụ: Netflix, Spotify, Disney+, HBO Max.

Thanh toán theo mức sử dụng (Pay-As-You-Go – PAYG)

Trả tiền theo từng lần sử dụng hay mức độ sử dụng thực tế (based on actual usage) ⟶ gọi là Pay-As-You-Go (PAYG).

Cụ thể PAYG nghĩa là “dùng bao nhiêu, trả bấy nhiêu”, ví dụ tính phí theo:

Số phút stream

Số lượt gọi API

Băng thông (bandwidth)

Dung lượng dữ liệu (GB) như dữ liệu di động (mobile data) hay dung lượng lưu trữ

Số lượt truy cập, lượt xem nội dung

Số tin nhắn SMS gửi đi

Điểm cốt lõi nằm ở logic tính phí theo usage (usage-based logic)

Không phải ở khả năng hủy dịch vụ bất kỳ lúc nào.

Nhiều người (kể cả trong tài liệu nội bộ hoặc truyền thông marketing) hay nhầm lẫn PAYG đồng nghĩa với “có thể hủy bất cứ lúc nào / không cam kết hợp đồng”

Cách hiểu ở trên hoàn toàn sai và không nắm bản chất ⟶ hiểu đúng phải là PAYG = “trả tiền theo mức sử dụng thực tế”

Dù có hạn sử dụng ⟶ nếu có logic PAYG thì vẫn là PAYG ví dụ “Gói 10GB hết hạn sau 30 ngày”.

Dạng lai (hybrid) ⟶ là kết hợp giữa thuê bao định kỳ và PAYG

Còn gọi là PAYG subscription hay “subscription có tùy chọn PAYG” (subscription with PAYG options)

Có nghĩa là thuê bao (fixed recurring payment) ⟶ để truy cập platform hay dịch vụ (mức phí tối thiểu)

Hóa đơn định kỳ sẽ tính dựa trên mức độ sử dụng (PAYG logic) ⟶ ví dụ số phút stream + base fee, hay bandwidth với CDN

Cách kết hợp này giúp cân bằng giữa doanh thu ổn định (base fee) và khả năng mở rộng theo nhu cầu thực tế của người dùng.

Đây là mô hình hay thấy của các các nền tảng trực tuyến SaaS (Software as a Service), ví dụ dịch vụ CDN tính phí base fee hàng tháng + băng thông (bandwidth) vượt mức.

Tóm lại có 3 loại chính như sau:

Table 2-1: Các mô hình thanh toán cơ bản

Với sự phát triển SaaS platforms và các dịch vụ đám mây, “mô hình lai” ngày càng trở nên phổ biến.

Riêng với dịch vụ streaming, thực tế luôn tồn tại cả hai nhóm thanh toán “fixed recurring subscription” và PAYG nhưng được phân tách và phân biệt rõ ràng:

Fixed recurring subscription

Là hình thức chính và gần như duy nhất ⟶ mô hình thuê bao.

Người dùng trả phí định kỳ cố định (theo tháng, quý, năm) để truy cập toàn bộ hoặc một phần thư viện nội dung.

Ví dụ: Netflix, Disney+, HBO Max, iQIYI, Tencent Video

Pay-As-You-Go (PAYG)

Dùng thanh toán theo từng nội dung hoặc thời hạn ⟶ cụ thể bao gồm:

Pay-per-view (PPV): mua quyền xem một sự kiện hoặc nội dung duy nhất (ví dụ trận bóng, concert).

Rental (thuê phim): trả tiền để xem trong một khoảng thời gian giới hạn (ví dụ 48 giờ).

Access pass (thẻ / vé truy cập): trả tiền để xem một nhóm nội dung hoặc sự kiện trong thời hạn xác định (ví dụ “EURO 2024 Access Pass” có hiệu lực từ 14/6 đến 14/7).

Tức rental chính là một dạng của TVOD (transactional). TVOD là khái niệm rộng hơn, bao gồm cả rental (thuê) và bao gồm cả EST (Electronic Sell-Through — mua sở hữu vĩnh viễn).

Access pass — nên hiểu thế nào?

Bản chất là vé truy cập tạm thời (temporary access) cho một nhóm nội dung hoặc một giai đoạn giới hạn thời gian.

Người dùng trả tiền một lần → được truy cập không giới hạn trong thời gian hiệu lực.

Có tính chất như một small subscription nhưng sau khi hết hạn, quyền truy cập tự động chấm dứt, không tự gia hạn.

Phân loại kỹ thuật ⟶ được phân loại thuộc nhóm PAYG.

Lưu ý: PAYG logic không liên quan hình thức thanh toán (chưa nói đến việc thanh toán như thế nào) ⟶ mà liên quan cách tính phí (charging logic) ⟶ mà là phải trả bao nhiêu.

Khi nào nên gọi là access pass chứ không phải subscription?

Table 2-2: Đặc điểm của Access pass

Trong lĩnh vực online streaming, subscription chỉ đúng khi có thanh toán định kỳ lặp lại (recurring). Còn các gói trả tiền một lần cho quyền truy cập có giới hạn thời gian hoặc nội dung, như rental, PPV, access pass, đều thuộc nhóm Pay-As-You-Go (PAYG).

Trả trước (prepaid) vs. trả sau (postpaid)

Prepaid (trả trước) và postpaid (trả sau) là hai hình thức thanh toán phổ biến phổ biến cho dịch vụ thuê bao. Hai hình thức này phân biệt nhau về mặt logic nghiệp vụ cụ thể là hành vi sử dụng (in behavior) chứ không phải theo dòng tiền (in cash flow).

Prepaid (trả trước)

Khách hàng thanh toán trước khi sử dụng dịch vụ.

Phù hợp với mô hình ngắn hạn, PAYG logic, không ràng buộc hợp đồng.

Ví dụ: thuê bao tháng trả trước, thẻ nạp xem phim, PPV hoặc gói streaming 30 ngày.

Postpaid (trả sau)

Khách hàng sử dụng dịch vụ trước và thanh toán sau, theo nguyên tắc “use now, pay later”.

Mô hình này thường gắn với hợp đồng (contract-based) và có cam kết.

Tức đây chính là mô hình truyền thống của các nhà mạng, truyền hình cáp, hoặc dịch vụ doanh nghiệp (enterprise subscription).

Lưu ý: “postpaid” ≠ đơn thuần là sẽ “trả tiền sau” ⟶ hiểu như vậy rất máy móc.

Khách hàng postpaid vẫn có thể thanh toán trước ⟶ gọi là upfront payment/settlement

Ví dụ “Thuê bao trả sau (có HĐ) thanh toán trước 12 tháng” ⟶ tương ứng mô tả tiếng Anh là “postpaid subscription with upfront payment”.

Upfront payment không phải là deposit, thường không được refund và sẽ khấu trừ vào hóa đơn hàng tháng

Với postpaid, khách hàng dùng trước, trả sau, nên nhà cung cấp chịu rủi ro tín dụng, do đó thường gắn với hợp đồng để ràng buộc nghĩa vụ thanh toán.

Ngược lại, hợp đồng cũng bảo vệ người tiêu dùng, đảm bảo chất lượng dịch vụ và quyền lợi theo quy định của cơ quan quản lý, nhất là trong lĩnh vực viễn thông và truyền hình trả tiền.

Nhu cầu xem truyền hình trên các thiết bị di động (gọi là out-of-home streaming hay off-net viewing) ngày càng gia tăng, làm cho prepaid càng trở nên phù hợp và thuận tiện hơn.

Dịch vụ online sẽ không cần việc triển khai dịch vụ cũng không tốn phí cài đặt hay cần thời gian chờ lắp đặt, triển khai.

Được gọi là “mô hình tiện lợi” (convenience model), prepaid giúp khách hàng không cần phải nhớ để thanh toán các giao dịch mua định kỳ.

Mô hình này không đặt nặng vấn đề về duy trì hợp đồng dài hạn, không bị ràng buộc bởi các cam kết hợp đồng (no contractual commitments), và cho phép hủy dịch vụ bất cứ khi nào mà không tốn phí hủy bỏ (no penalty for cancellation).

Khách hàng kiểm soát tốt hơn về chi tiêu mà không phải lo lắng về việc thanh toán hóa đơn sau này.

Với việc yêu cầu người dùng trả tiền trước, nhà cung cấp dịch vụ cũng tránh rủi ro không thu được tiền sau khi dịch vụ đã được cung cấp.

Prepaid (trả trước) vẫn có thể áp dụng thanh toán định kỳ (recurring payment) thông qua tính năng tự động gia hạn (auto-renewal).

Cách này giúp duy trì dịch vụ liên tục (tránh gián đoạn do quên thanh toán) mà không cần thao tác thủ công mỗi chu kỳ.

Giúp khách hàng tránh bị gián đoạn dịch vụ (service interruption prevention) do quên thanh toán.

Bản chất vẫn là thanh toán trước và sử dụng sau ⟶ chỉ khác là quy trình thanh toán được tự động hóa thay vì thủ công.

Hệ thống quản lý thuê bao (subscriber management system – SMS)

Quản lý đăng ký thuê bao (subscriber management) là một quy trình để quản lý khách hàng từ khi họ đăng ký sản phẩm hoặc dịch vụ (subscribe to a product or service) cho đến khi họ hủy đăng ký (cancel the subscription).

Dễ thấy chức năng cơ bản của SMS là:

Đăng ký dịch vụ (subscription enrollment)

Xử lý quá trình thanh toán (payment processing)

Quản lý truy cập (access control management)

Tính cước (billing)

Giám sát việc sử dụng (usage monitoring)

Ngoài ra, SMS có các chức năng khác như quản lý gói (dịch vụ), gửi email & thông báo (email & notification), và dịch vụ khách hàng (customer services – CS). Hiện nay với sự phát triển của hệ thống của “hệ thống quản lý quan hệ khách hàng” (customer relationship management – CRM) thì các chức năng liên quan đến khách hàng (customer facing hay customer-related) sẽ được gom về CRM, có thể tách biệt hoặc là chức năng con nằm trong SMS.

Theo “Khung quy trình nghiệp vụ” (Business Process Framework) hay “Bản đồ tiêu chuẩn hóa hoạt động của ngành viễn thông”, còn gọi là (enhanced Telecom Operations Map – eTOM) được chuẩn hóa trong ITU-T M.3050 (2007-03), SMS sẽ tương ứng với hai phần là CRM và “Quản lý & vận hành dịch vụ” (service management and operations – SM&O).

Figure 2-2: Business Process Framework (eTOM) – Level 0

Quản lý gói dịch vụ (tạm dịch cho offer management) trong bối cảnh hệ thống viễn thông (telco), truyền hình trả tiền (pay-TV), hoặc nền tảng SaaS, đề cập đến quá trình tạo ra, quản lý và tối ưu hóa các gói dịch vụ (plans and packages) cung cấp cho khách hàng. Cách thiết kế gói dịch vụ, bao gồm cả khuyến mãi (promotion), thể hiện chiến lược về giá (pricing) của doanh nghiệp, nhằm phản ánh chiến lược kinh doanh tổng thể. Mục tiêu chính của quản lý gói dịch vụ (offer management) là thu hút khách hàng, tối đa hóa doanh thu/lợi nhuận và nâng cao sự hài lòng.

Theo eTOM, thì “quản lý gói dịch vụ” có tên đầy đủ “Marketing & Offer management”, nằm ở giai đoạn Chiến lược và Thiết kế dịch vụ (strategy & design). Trong khi đó, SMS như đã nó ở phần trên sẽ nắm vai trò của triển khai và vận hành (deployment & operations). Các quyết định về gói dịch vụ và giá cả cũng như khuyến mãi sẽ ảnh hưởng trực tiếp đến cách thức quản lý thuê bao (subscriber management).

Truyền phát video trực tuyến (video streaming)

Hệ thống truyền phát video (video streaming) phải qua nhiều giai đoạn nối tiếp (video delivery pipeline) trước khi nội dung đến được đến thiết bị của người xem bao gồm:

Thu nhận nội dung (acquisition hay ingestion)

Mã hóa/chuyển mã (encoding/transcoding)

Mật mã hóa (encryption)

Đóng gói (packaging, để phù hợp cho streaming)

Phân phối (distribution)

Chèn quảng cáo phía máy chủ (server-side ad insertion) ...

Để hiểu rõ hơn, cần xem xét chi tiết luồng nội dung (content flow) — tức quá trình video và âm thanh đi từ nguồn đến người xem cuối cùng. Content flow cũng thể hiện luồng tác vụ cần thực hiện với video (video workflow) trong quá trình phân phối.

Note: Khi nói “streaming” có nghĩa ngầm định là phân phối nội dung qua Internet (over-the-top, OTT). Xem thêm [2.3.13 — Streaming].

Quy trình xử lý nội dung (content workflow)

Về cơ bản content flow (hay video workflow) có thể được chia thành ba giai đoạn chính:

Chuẩn bị (preparation) — Bao gồm tất cả các bước cần thiết để tạo ra nội dung. Giai đoạn này có thể được chia nhỏ thành:

Thu thập/thu nhận vào (acquisition/ingestion) — Nội dung được đưa vào hệ thống từ nhiều nguồn khác nhau có thể là nguồn trực tiếp như từ camera (hay luồng video – video stream) hoặc nội dung đã ghi trước (files).

Chỉnh sửa, xử lý (manipulation) — Nội dung sau khi vào hệ thống được sẽ được xử lý, chỉnh sửa tạo ra sản phẩm cuối cùng.

Trong quá trình này các tác vụ sản xuất video (video production) cần sự tham gia trực tiếp của con người và không hoàn toàn tự động hóa. Video production trong ngữ cảnh này không phải là quay phim, viết kịch bản hay dựng phim.

Các tác vụ khác như mã hóa hoặc chuyển mã (encoding/transcoding), mật mã hóa (encryption) để bảo vệ nội dung, đóng gói (packaging) thường được tự động hóa cao.

Phân phối (delivery/distribution) — Bao gồm việc truyền tải nội dung đã chuẩn bị qua các kênh phân phối đến người xem cuối cùng.

Trình diễn/tiêu thụ (presentation/consumption) — Giai đoạn cuối cùng, nơi nội dung video được phát và tiêu thụ/trải nghiệm bởi người xem cuối cùng.

Ví dụ rút gọn giai đoạn chuẩn bị như sau:

Thu thập: upload tập tin video lên hệ thống

Xử lý:

Thêm tiêu đề cho video và mô tả nội dung video.

Thêm hashtag để giúp tìm kiếm và gợi ý.

Thêm phụ đề

Tạo hình thu nhỏ (thumbnail)

Hệ thống tự động thêm định dạng phù hợp nhiều nền tảng.

Figure 2-3: Video streaming — Content flow

Sản xuất nội dung (video production)

Quy trình video production cũng sẽ chia làm 2 loại tùy thuộc nội dung có phải là nội dung phát trực tiếp hay không (có phải live content, hay in real-time hay không):

Sản xuất hậu kỳ (post-production) — Tập trung vào việc hoàn thiện và tinh chỉnh nội dung video dạng tập tin.

File ingesting — Nhận và đưa các tập tin video vào hệ thống

Editing — Chỉnh sửa video, bao gồm cắt ghép, điều chỉnh thời gian và thứ tự âm thanh, metadata.

Graphic/color correction — Điều chỉnh màu sắc.

FX (visual effects) — Hiệu ứng đặc biệt về hình ảnh và đồ họa.

Sound design, audio — Hiệu ứng âm thanh, âm nhạc nền, và điều chỉnh âm lượng

Dubbling/subtitling — Thêm, bổ sung các bản lồng tiếng, thuyết minh hoặc phụ đề.

Conforming — Đảm bảo nội dung tuân thủ quy định, kiểm duyệt nội dung không phù hợp hoặc vi phạm bản quyền (censorship).

Rendering — Kết xuất video hoàn chỉnh và xuất ra định dạng phù hợp

QC/report — Kiểm tra chất lượng và báo cáo.

Approval — Nhận phê duyệt cuối cùng.

Sản xuất trực tiếp (live production) — Tập trung vào việc thu nhận và phát sóng video trực như sự kiện trực tiếp, chương trình truyền hình, hoặc livestream.

Live ingestion — Nhận và xử lý luồng video trực tiếp từ các nguồn phát sóng hoặc thiết bị ghi hình. Đây là công việc của bộ phận head-end.

Live editing — Quá trình từ quay, chỉnh sửa đến phát sóng được thực hiện đồng bộ theo thời gian thực, thường diễn ra tại studio. Do quy trình sản xuất trực tiếp (live production) thường thực hiện với môi trường studio nên còn được gọi là sản xuất phòng thu trực tiếp (live studio production).

Broadcast management — Quản lý việc phát sóng và điều phối các yếu tố truyền hình trực tiếp.

Time-shifting/recording — Xử lý và ghi lại video để phát lại sau.

Các bước chính tiêu biểu của post-production có thể thể hiện bởi hình sau

Figure 2-4: Video workflow — Các bước chính tiêu biểu của post-production

Sự khác biệt giữa sản xuất hậu kỳ và sản xuất trực tiếp chủ yếu hai yếu tố chính là thời gian và công cụ sử dụng:

Table 2-3: Khác biệt giữa sản xuất hậu kỳ và sản xuất trực tiếp

Quá trình phân phối (video delivery pipeline)

Như vậy nếu tạm thời lược bớt các công đoạn liên quan nhiều đến con người như video production, các bước trước khi đến người dùng sẽ chủ yếu liên quan đến xử lý (processing), lưu trữ (storage) và phân phối (distribution/delivery) video bao gồm:

Thu nhận nội dung (acquisition/ingestion) — Đưa nội dung từ camera (hay các nguồn trực tiếp khác) hoặc từ các tập tin (files) vào hệ thống.

Mã hóa hoặc chuyển mã (encoding/transcoding) — Chuyển mã để phù hợp với nhiều thiết bị và mạng khác nhau (xem mục [2.3.6 — Transcoding]).

Mật mã hóa (encryption, dùng mật mã hóa để phân biệt với encoding) — Bảo vệ nội dung bằng cách mật mã hóa.

Đóng gói (packaging) — Định dạng lại nội dung để phù hợp với các giao thức truyền phát streaming ví dụ như HLS, DASH.

Phân phối (distribution/delivery) — Thường được thực hiện qua hệ thống mạng phân phối nội dung (CDN).

Origin/storage — Đầu tiên là lưu trữ nội dung trên các “máy chủ (lưu trữ) nguồn” (origin servers hay đơn giản gọi là origin)

Caching — Sau đó phân phối đến các “máy chủ biên” khác của mạng CDN (CDN edge servers).

Ghép quảng cáo “trực tiếp” vào video phía máy chủ (tạm dịch cho ad stitching)

Server-Side Ad Insertion (SSAI) và Dynamic Ad Insertion (DAI) là tên hai thuật ngữ về công nghệ chính trong lĩnh vực chèn quảng cáo phía server (xem thêm phần [2.3.34 — SSAI & DAI]).

SSAI cho phép “ghép quảng cáo” vào video ngay từ phía server, tạo thành một luồng duy nhất (single video stream), trước khi nội dung được truyền phát đến thiết bị của người xem (xem thêm phần [2.3.32 — Ad stitching (ads)]).

DAI nhấn mạnh khả năng chèn quảng cáo “động” (dynamic), lựa chọn quảng cáo phù hợp dựa trên nhiều tiêu chí (based on various targeting criteria), với dữ liệu theo thời gian thực. Ví dụ, quảng cáo có thể được chọn để tối ưu hóa lợi nhuận, đồng thời cá nhân hóa dựa trên người xem và thiết bị.

SSAI là phương pháp chủ đạo, được sử dụng phổ biến để thực hiện tính “dynamic” của DAI. Do đó, DAI thường được sử dụng như một từ đồng nghĩa với SSAI.

Recording — Ghi lại video để sử dụng sau.

Trong hệ thống dịch vụ IPTV, nội dung phát trực tiếp (tức live content như kênh truyền hình, sự kiện trực tiếp) được phân phối (distribution) qua “mạng được quản lý” (managed network).

Phân phối nội dung qua mạng được quản lý (managed network) của nhà cung cấp.

Không phụ thuộc Internet công cộng ⟶ đảm bảo ổn định và kiểm soát chất lượng.

Đồng thời, việc bảo vệ nội dung cũng sử dụng một công nghệ khác ⟶ gọi là “hệ thống truy cập có điều kiện” (conditional access system – CAS) thay vì dùng “quản lý quyền kỹ thuật số” (digital rights management – DRM) như trong streaming qua Internet.

Trong khi đó online streaming = Internet-based (OTT)

Truyền phát nội dung qua Internet công cộng ⟶ không cần hạ tầng mạng riêng.

Dùng công nghệ gọi là DRM để bảo vệ nội dung.

Note: Tóm lại theo phân loại kỹ thuật, IPTV (là một bộ các công nghệ khác) không được xem là “streaming” ⟶ mà được gọi là “non-streaming”.

Nhiều telco / pay-TV operator ban đầu cung cấp IPTV (non-streaming) trên mạng được quản lý (managed network). Sau đó, họ mở rộng sang OTT / online streaming (tức qua Internet) để hỗ trợ xem ngoài managed network (out-of-home / off-net viewing).

Với việc mở rộng và đa dạng hóa dịch vụ, các nhà cung cấp thường áp dụng một kiến trúc hợp nhất để tích hợp cả IPTV và online streaming:

Tích hợp song song IPTV (non-streaming) và streaming trong cùng một hạ tầng kỹ thuật

Sử dụng CAS + DRM tùy theo kênh phân phối.

Giúp tối ưu vận hành, thống nhất quản lý nội dung, thuê bao và quảng cáo.

Sơ đồ một hệ thống video platform kết hợp IPTV (non-streaming) và (online) streaming thông thường sẽ như sau

Figure 2-5: Video platform kết hợp IPTV (non-streaming) và (online) streaming

Thuật ngữ và khái niệm cơ bản (glossary of terms and essential concepts)

Phần này chỉ liệt kê các khái niệm, định nghĩa và thuật ngữ ở mức cơ bản để giúp người đọc nắm bắt và giao tiếp hiệu quả với nội dung của tài liệu.

Bitrate

Tốc độ bit (bitrate) còn gọi là data rate là (lưu) lượng dữ liệu truyền đi hay nói cách khác là được sử dụng để truyền tải video trong mỗi giây và đo bằng đơn vị kilobit trên giây (kbps). Bitrate có thể là ổn định (còn gọi là hằng số – constant) hoặc thay đổi (variable), tùy vào cách transcode và mục đích sử dụng.

Constant Bitrate (CBR) — Bitrate được giữ ổn định (cố định) trong suốt quá trình streaming video, đảm bảo chất lượng video ổn định nhưng có thể không tối ưu hóa cho các phần nội dung khác nhau.

Variable Bitrate (VBR) — Bitrate thay đổi tùy theo mức độ phức tạp của từng khung hình, sẽ giúp tối ưu hóa dung lượng và chất lượng video.

Bitrate càng cao thì chất lượng video thường tốt hơn, nhưng cũng yêu cầu băng thông lớn hơn. Việc nâng cao “trải nghiệm” của user thường đi kèm với việc phải nâng cao độ phân giải (resolutions, hay kích thước khung hình), tốc độ khung hình (frame rates) › yêu cầu cao hơn về băng thông (bandwidth) › có khả năng gây tắt nghẽn băng thông (bandwidth congestion) liên quan trực tiếp đến độ trễ (latency). Bộ ba tam giác (bất khả thi) của video encoding (triangle of video encoding and streaming considerations/trade-offs) diễn đạt để mô tả mối quan hệ cân bằng giữa ba yếu tố chính trong video encoding:

Chất lượng hình ảnh (picture quality)

Bitrate hay chính xác là hiệu quả băng thông (bandwidth efficiency)

và độ trễ (latency)

Chỉ có thể tối ưu được hai trong ba yếu tố này, và việc cải thiện một yếu tố thường sẽ gây ảnh hưởng tiêu cực đến ít nhất một yếu tố còn lại.

Mezzanine (files)

Mezzanine files là các tập tin trung gian (intermediate files) có chất lượng cao, được lưu trữ để sử dụng trong quá trình sản xuất và phân phối nội dung. Tập tin này này có độ phân giải cao hơn và chất lượng tốt hơn so với các tập tin đầu ra cuối cùng (dùng để phát trực tuyến), nhưng lại có kích thước nhỏ hơn so với các source gốc không nén hoặc ít nén.

Nói chung, mezzanine là tập tin đầu vào sau biên tập của nội dung với đặc điểm:

Chất lượng cao — Giữ chất lượng cao của nội dung, giúp đảm bảo rằng các bản transcode và phân phối cuối cùng sẽ có chất lượng tốt nhất có thể.

Tối ưu dung lượng lưu trữ — Dạng trung gian phải có kích thước hơn so với các source gốc không nén hoặc nén ít (nhưng không cần thiết). Việc chuyển sang định dạng trung gian giúp tiết kiệm không gian lưu trữ mà vẫn đảm bảo chất lượng.

Linh hoạt khi sử dụng — Mezzanine files được xem là tài sản truyền thông (media assets) cần được format để quản lý và không cần phải tạo ra nhiều phiên bản khác nhau.

Codecs

Codec (viết tắt từ COder/DECoder) là thuật ngữ dùng chỉ một thuât toán (hay một bộ các thuật toán) định nghĩa việc nén và giải nén video và/hoặc audio (âm thanh). Với video thô, không nén (raw, uncompressed video) sẽ yêu cầu sử dụng bandwidth rất lớn và thường chỉ phù hợp để truyền qua cáp như HDMI, HD-SDI hoặc Ethernet. Dưới đây là bảng ví dụ cho thấy bitrate yêu cầu tương ứng với từng độ phân giải của video gốc.

Table 2-4: Ví dụ yêu cầu về bitrate của video chưa nén (raw video data)

Không thể truyền tải 1.5 Gbps đến thiết bị di động của người dùng qua Internet, bởi vì hầu hết các kết nối Internet (trên thế giới) cũng không thể đáp ứng tốc độ như vậy. Video bắt buộc phải được nén để giảm tốc độ bit xuống mức khả thi hơn, thường trong phạm vi từ 1 đến 20 Mbps. Việc nén video (video compression) được thực hiện nhờ các codec, giúp giảm kích thước tập tin và tốc độ bit trong khi vẫn giữ chất lượng video ở mức chấp nhận được.

Một số video codecs chính và phổ biến (major codecs) có thể kể là:

H.264 hay chính xác là H.264/Advanced Video Coding (AVC) còn gọi là MPEG-4 AVC hay MPEG-4 Part 10 (tiêu chuẩn hóa ISO/IEC trong ISO/IEC 14496-10).

H.265 tức High Efficiency Video Coding (HEVC)/H.265 tiêu chuẩn hóa với tên là MPEG-H Part 2 (tiêu chuẩn hóa ISO/IEC trong ISO/IEC 23008-2).

AV1 (AOMedia Video 1) một codec video mở và miễn phí, được phát triển bởi Alliance for Open Media (AOM)

Codec âm thanh phổ biến

AAC (Advanced Audio Codec) tiêu chuẩn hóa trong MPEG-4 Part 3 [ISO/IEC 14496-3] và MPEG-2 Part 7 [ISO/IEC 13818-7]

MP3 (MPEG-1 or 2 Layer 3) tiêu chuẩn hóa trong MPEG-2 Part 3 [ISO/IEC 13818-3]

Vorbis/Opus (OGG) hai codec âm thanh mở và miễn phí thường được sử dụng trong định dạng container OGG

Free Lossless Audio Codec (FLAC)

Họ các codec của Dolby như Dolby Digital (AC-3), Dolby Digital Plus (EAC-3 hay EC-3)

Containers (format)

Container hay container format là một định dạng hoặc cấu trúc dùng để kết hợp nhiều loại thông tin khác nhau vào một nguồn duy nhất. Các loại thông tin này có thể bao gồm video, âm thanh, metadata, và đôi khi cả phụ đề. Mục đích của container format ban đầu là để lưu trữ các dữ liệu này trong dưới dạng tập tin nên còn có tên gọi là container file formats hay kiểu tập tin/dạng tập tin (file types). Sau này, container format còn dùng để tổ chức truyền tải dữ liệu qua mạng tức dưới dạng byte-stream data format, đặc biệt là cho streaming gọi là container format for streaming. Tuy nhiên, tên gọi container file format vẫn có thể được sử dụng cho cả hai trường hợp dù là dùng cho lưu trữ dạng file hay dùng để streaming.

Một số định dạng container video phổ biến lưu trữ dưới dạng tập tin:

MP4 (MPEG-4 Part 14) còn gọi là MPEG-4 phổ biến và tương thích cao với hầu hết các player và thiết bị trên web và các di động. MP4 hỗ trợ hầu hết các codec thông dụng với video codec là H.264/AVC, HEVC/H.265, AV1, VP9 và audio codec là MP3, AAC, Opus, AC3, FLAC ...

Matroska (MKV) container format mở và miễn phí cũng hỗ trợ nhiều codec video và audio, bao gồm H.264, H.265, AAC, MP3 …

WebM một container format do Google phát triển hỗ trợ video codec như VP9, AV1 và audio codec như Opus.

Ogg một container format ở và miễn phí của Xiph.org Foundation chủ yếu dùng với codec âm thanh như Vorbis và Opus

Bản thân các audio codec thường đi kèm với cách lưu trữ dữ liệu âm thanh dưới dạng các tập tin âm thanh. Điều này có nghĩa là các audio codec thường quy định cả container format. Do đó, tên của audio codec có thể được sử dụng như một cách để chỉ cả codec và container format gọi chung là “audio coding format” (khi không cần phân biệt là codec hay container).

Container dành cho streaming đầu tiên có thể kể là MPEG Transport Stream, còn được biết với tên khác như TS hay MTS, được tiêu chuẩn hóa ISO/IEC trong ISO/IEC 13818-1. MPEG-2 TS là cách gọi cụ thể hơn, chỉ định rằng ngữ cảnh của việc tiêu chuẩn hóa thuộc về MPEG-2 (ví dụ MPEG-1 không có tiêu chuẩn về nén nhiều luồng âm thanh stereo). MPEG-2 TS vốn được phát triển cho việc phát sóng video (broadcasting) qua mạng mặt đất và vệ tinh (terrestrial and satellite networks như trong các hệ thống Digital Video Broadcasting – DVB, Advanced Television Systems Committee – ATSC và Internet Protocol Television – IPTV), cũng như cho lưu trữ và phân phối thông qua các phương tiện vật lý (physical media, như đĩa Blu-ray). Apple, sau đó, đã chọn TS làm container format cho HLS khiến TS trở thành một định dạng quan trọng trong lĩnh vực streaming.

Xem thêm

Web video codec guide - Web media technologies | MDN (mozilla.org)

Web audio codec guide - Web media technologies | MDN (mozilla.org)

Encoding

Mã hóa (encoding) hay nén (compression) là quá trình loại bỏ các phần dư thừa hay các phần không quá cần thiết từ dữ liệu video và audio thô (raw video and audio data) tức dữ liệu chưa được mã hóa hay chưa nén (uncompressed video). Mục đích của quá trình encoding là giảm lượng dữ liệu cần thiết để lưu trữ hay truyền tải qua mạng, qua các phương tiện khác nhau (ví dụ đĩa vật lý, USB …) hay tới thiết bị phát (playback device). Quá trình này có thể dẫn đến việc giảm chất lượng hình ảnh hoặc âm thanh, nhưng sự mất mát thường không đáng chú ý, hay chấp nhận được đối với người dùng.

Có nghĩa, encoding là quá trình sử dụng codec để chuyển đổi dữ liệu thô (chẳng hạn như video hoặc âm thanh) thành định dạng đã mã hóa (gọi là encoded hay compressed).

Lưu ý: cần phân biệt giữa mã hóa (encoding) với mật mã hóa (encryption) vì nhiều khi encryption vẫn được dịch là mã hóa.

Mật mã hóa (encryption) là thuật ngữ dùng chỉ quá trình chuyển đổi thông tin từ dạng thông thường có thể đọc được (tức sử dụng được nói chung, nếu dữ liệu text thì gọi là plaintext) sang dạng không đọc được (đã được mật mã hóa – encrypted, với text gọi là ciphertext) nhằm bảo mật thông tin. Mật mã hóa luôn sử dụng một khóa (key) đóng vai trò quan trọng trong việc bảo vệ dữ liệu. Khóa này có thể là khóa đối xứng hoặc khóa bất đối xứng. Chỉ khi có khóa phù hợp, quá trình giải mật mã (decryption) mới có thể khôi phục thông tin đã được mật mã hóa về trạng thái ban đầu.

Trong khi đó mã hóa (encoding) chỉ là một cách biến đổi thông tin nhằm mục đích nhất định mà có thể dễ dàng chuyển đổi ngược lại về dạng ban đầu.

Transcoding

Chuyển mã (transcoding) là quá trình chuyển đổi định dạng của một media file (ví dụ mezzanine) hay stream, đã được mã hóa (gọi là encoded hay compressed) thường là từ một định dạng mã hóa (codec) này sang định dạng khác (codec khác).

Transcoding không chỉ áp dụng cho việc chuyển đổi giữa các codec khác nhau, nó cũng dùng để chỉ việc chuyển đổi sử dụng cùng codec nhưng với tập thông số khác nhau. Có nghĩa transcoding sẽ thực hiện giải nén (decompressing với input video codec), thay đổi/chuyển đổi (altering) theo các thông số chỉ định và sau đó mã hóa hay nén lại với codec được chỉ định (output video codec).

Encoding tập trung vào việc chuyển đổi dữ liệu gốc sang định dạng mã hóa. Trong khi đó transcoding là chuyển đổi giữa các định dạng mã hóa khác nhau đã có sẵn.

Muxing (multiplexing)

Muxing (là viết tắt của multiplexing), tạm dịch là “ghép kênh”, là quá trình nhận nhiều nguồn hay tính hiệu đầu vào độc lập với nhau (multiple independent inputs/signals) và đóng gói chúng lại với nhau thành một nguồn hay một luồng tín hiệu đầu ra duy nhất (single output/signal) để có thể truyền tải qua một kênh truyền chung (shared medium).

Thuật ngữ muxing/multiplexing (ghép kênh) có lịch sử lâu đời trong ngành viễn thông khi thực hiện truyền đồng thời nhiều cuộc gọi hoặc tín hiệu trên cùng một phương tiện vật lý, như dây điện thoại.

Trong việc xử lý video kỹ thuật số (digital video processing), muxing sẽ kết hợp đầu vào video và audio (video and audio inputs), metadata và những dữ liệu khác nếu có (như phụ đề) lại với nhau thành một container duy nhất. Mỗi loại nội dung như video hay audio là một dòng hay luồng dữ liệu cơ bản gọi là elementary stream. Container có thể là dạng tập tin hoặc dạng container dùng để streaming (tức dạng byte-stream data).

Các elementary streams là các thành phần cuối (nốt lá) trong cấu trúc phân cấp multiplexing. Chúng không phải là kết quả của một quá trình multiplexing trước đó mà là các luồng dữ liệu độc lập, chứa nội dung đã được mã hóa (encoded media) như video hoặc audio. Nghĩa là chúng không thể được tách nhỏ hơn nữa (không thể demultiplexed).

Quá trình muxing, mặc dù phức tạp, nhưng chủ yếu là việc tổ chức và sắp xếp dữ liệu để lưu trữ hoặc vận chuyển. Dữ liệu sau khi muxing cũng bao gồm thông tin cần thiết để xác định thời điểm trình bày của từng stream. Điều này có nghĩa là muxing liên quan trực tiếp đến việc đồng bộ thời gian (time synchronization). Việc đồng bộ thời gian là cực kỳ quan trọng trong quá trình phát lại (playback). Khi muxing được thực hiện đúng, âm thanh sẽ khớp với video, phụ đề sẽ khớp với lời thoại, nghĩa là mọi thứ kết hợp để mang đến một trải nghiệm đồng bộ không bị lệch nhịp.

Demuxing (demultiplexing)

Demuxing (viết tắt của demultiplexing, tạm dịch là “tách (ghép) kênh”) đơn giản là quá trình ngược lại của muxing/multiplexing. Nó sẽ thực hiện tách một tín hiệu hay một stream riêng lẻ (single signal/stream) vốn đã được “ghép kênh” trước đó (muxed), thành các tín hiệu hay đầu vào gốc.

I-frame (video)

Khái niệm cốt lõi (fundamental concept) trong việc nén và phân phối video (video compression and delivery) là việc tìm cách loại bỏ các hình ảnh không cần thiết (eliminating redundancies) trong một chuỗi các hình ảnh mà không làm ảnh hưởng quá lớn đến chất lượng (tức trong mức độ chấp nhận được).

Thông thường trong một loạt các khung hình (frames of video) thì phần lớn hình ảnh (large portion of the image) là rất giống nhau.

Bộ nén video (encoder) sẽ tận dụng điều này bằng cách đầu tiên gửi một frame đầy đủ gọi là keyframes và sau đó gửi các frame chỉ bao gồm các phần thay đổi gọi là subsequent frames.

Tại bên nhận (receiver hay cụ thể là decoder) sẽ thực hiện quá ngược lại để tái tạo (re-create) hình ảnh mong muốn.

Phương pháp nén này gọi là temporal compression (tạm dịch là “nén theo thời gian” vì thông tin video thay đổi theo thời gian).

Loại nén thứ hai được sử dụng gọi là spatial compression (tạm dịch là “nén theo không gian”) được áp dụng cho chính keyframes.

Spatial compression loại bỏ các phần dư thừa trong hình ảnh của keyframes.

Ví dụ các pixel xung quanh giống với một pixel trong hình sẽ được nhóm lại thành một group các pixel khi truyền đi.

Phần này sử dụng chủ yếu các kỹ thuật như trong việc nén ảnh (image compression) ví dụ JPEG format.

I-frames (intra frames) là một loại khung hình đặc biệt trong kỹ thuật nén video.

Một I-frame sẽ không phụ thuộc vào bất kỳ khung hình nào trước hoặc sau nó để tạo ra một hình ảnh hoàn chỉnh.

Chứa tất cả thông tin cần thiết để tái tạo hình ảnh mà không cần tham chiếu đến các khung hình khác.

Đóng vai trò là các keyframes giúp duy trì chất lượng, truyền phát và playback video.

Group of Pictures (GOP) size

Group of Pictures (GOP) như tên gọi là một nhóm các ảnh (sử dụng trong các codec như H.264/MPEG-4 AVC tức MPEG-4 Part 10 hay HEVC/H.265 tức MPEG-H Part 2). GOP size chính xác là khoảng cách giữa 2 keyframes được tính bằng số lượng frames. Một GOP thường bao gồm các khung hình I-frame (khung hình chính), P-frame (khung hình dự đoán), và B-frame (khung hình hai chiều).

I-frames (intra frames) — Khung hình chính (keyframes), độc lập, chứa toàn bộ thông tin hình ảnh mà không phụ thuộc vào khung hình khác.

P-frames (predictive frame) — Khung hình dự đoán, chỉ lưu thông tin về sự thay đổi so với khung hình trước đó.

B-frames (bidirectional frame) — Khung hình hai chiều, lưu thông tin về sự thay đổi so với khung hình trước và sau.

Như đã nói về lý thuyết thì lý tưởng nhất thì encoder sẽ gửi một keyframe và các subsequent frames chỉ gửi những thông tin thay đổi. Tuy nhiên việc implement trong thực tế không thể thực hiện hoàn hảo như vậy bởi nhiều lý do trong đó có thể kể hai lý do chính như sau:

Truy cập ngẫu nhiên (random access) — Việc gửi keyframe đầu tiên và gửi các subsequent frames chỉ bao gồm những thay đổi chỉ áp dụng khi người xem từ đầu và chỉ xem tới (forward).

Đây không phải là cách xem duy nhất. Viewer có thể skip, hay seek tới một điểm bất kỳ.

Cần nhiều keyframe hơn để cho phép viewer có thể xem từ điểm đã chọn.

Khả năng sửa lỗi/phục hồi lỗi (error resiliency) — Một điều thực tế là việc truyền video không hoàn hảo.

Các gói tin có thể bị mất trong quá trình truyền và còn rất nhiều các lỗi khác.

Một khi có lỗi hay hư hỏng (corruption), nếu chỉ truyền thay đổi (differences) lỗi này sẽ lan truyền trong video stream cho đến khi gặp keyframe khác.

Thêm keyframes là cách dễ nhất để tăng tính phục hồi lỗi, giúp decoders nhận biết keyframe này là một “known good” frame để xóa đi lỗi bị lan truyền trước đó.

Có thể để ý điều này khi xem phim, gặp tình trạng giật hình (choppy), ám xanh (green-tinged) rồi hình ảnh đột nhiên trở lại bình thường và sắc nét.

GOP size là một yếu tố quan trọng trong việc điều chỉnh hiệu suất nén video và chất lượng hình ảnh, kích thước file, tốc độ phát, và khả năng phục hồi lỗi của video. Các ảnh hưởng cụ thể có thể liệt kê như sau:

Ảnh hưởng chất lượng & lưu trữ — GOP dài (nhiều khung hình giữa các I-frames) có thể giảm kích thước file và băng thông, nhưng sẽ làm giảm khả năng phục hồi chất lượng khi có lỗi hoặc mất dữ liệu. GOP ngắn (ít khung hình giữa các I-frames) có thể cải thiện chất lượng và khả năng phục hồi lỗi, nhưng có thể làm tăng kích thước file. Cần phải cân nhắc giữa chất lượng video và hiệu suất nén.

Ảnh hưởng streaming — GOP size ảnh hưởng đến việc streaming nhất là trong các tình huống trực tiếp (live streaming). GOP ngắn sẽ giúp giảm độ trễ và cải thiện khả năng đồng bộ hóa.

Timecode

Renditions

Rendition là một phiên bản hay biến thể (variant) của một “tài sản gốc” (tức mezzanine files, mezzanine assets), đã được định dạng (thông qua quá trình chuyển mã – transcoding) với các thông số cụ thể như về độ phân giải (resolution), tốc độ khung hình (frame rate), hoặc chất lượng (quality) ... Các rendition được tạo ra để đáp ứng các yêu cầu sử dụng cụ thể ví dụ tối ưu cho từng nền tảng phân phối (web, phone, tablet, hay smart TV), để tiết kiệm băng thông và tài nguyên (xử lý) … hay với mục tiêu nhất định nào đó như dành cho download-to-go.

Thuật ngữ “profile” (chính xác hơn là “encoding/transcoding profile”) thường dùng để chỉ một “template” hoặc “cấu hình” đã xác định sẵn (pre-defined) sử dụng với các công cụ encode/transcode nhằm tạo ra các renditions. Cụ thể, profile là một tập hợp các thông số để điều chỉnh cách thức encode/transcode. Các thông số này có thể bao gồm bitrate, độ phân giải, tốc độ khung hình, và các đặc điểm khác liên quan đến codec. Profile thường được đặt một cái tên ngắn gọn và dễ hiểu nhưng thường có bao gồm thông tin về resolution ví dụ “H.264 HD”, “720p – All iPad”, “1080p – YouTube”, hay “1080p – H.264 – Web”.

Việc sử dụng thuật ngữ profile và đặt tên cho profile cũng ảnh hưởng đến cách để truyền thông cho người dùng cuối (end-user) về chất lượng video, ví dụ chất lượng 720p hay 1080p (HD).  Tuy nhiên, profile lúc này thực chất lại là tên gọi “một hay một nhóm các renditions” được sử dụng. Cụ thể, khi user chọn chất lượng hình ảnh là 1080p, user cũng không thể biết rằng bên dưới có thể có đến 2-3 renditions có cùng resolution 1080p (nôm na là họ đang chọn nhóm profile có tên “1080p”):

Một vài thông số chính như 1920 × 1080p, 25/30/50/60 fps, chroma 4:2:0/4:2:2/4:4:4, bitrate thường từ 3-4 Mbps đến 8 Mbps

User sẽ không nắm chính xác chất lượng 1080p là 1080p @ 5 Mbps hay 1080p @ 7 Mbps hay codec sử dụng là gì.

Chưa kể các advanced settings/specs của audio đi cùng

Các rendition sẽ được liệt kê trong trong “tập tin kê khai” (cụ thể là adaptive streaming set của manifest, xem phần thuật ngữ “manifest” và “adaptive streaming protocols”) để player có thể chọn nội dung có chất lượng tốt nhất phù hợp với tốc độ kết nối Internet.

Streaming

Streaming (tạm dịch là “truyền phát video”) là một thuật ngữ chỉ quá trình truyền tải nội dung (video, âm thanh) qua Internet để người dùng có thể xem hoặc nghe ngay lập tức mà không cần tải toàn bộ về thiết bị.

Vì được thực hiện qua Internet, nó còn được gọi là online streaming (hay còn gọi là trực tuyến).

Lưu ý: “trực tuyến” = online khác với “trực tiếp” = live.

Streaming cũng có thể dùng như một thuật ngữ chỉ tập các công nghệ và phương thức truyền tải nội dung trực tuyến.

Khác với phương thức download truyền thống, trong đó toàn bộ dữ liệu được tải xuống trước khi phát, streaming sẽ chia nhỏ nội dung thành từng đoạn và được gửi liên tục hay truyền liên tục đến người dùng. Điều này giúp người dùng có thể bắt đầu xem nội dung ngay khi các phân đoạn nội dung được truyền tới, trong khi các phân đoạn tiếp theo vẫn đang tiếp tục tải xuống.

Hiện nay, có hai phương thức chính là live streaming (truyền phát trực tiếp) và on-demand streaming (truyền phát theo yêu cầu).

Live streaming cho phép truyền tải nội dung theo thời gian thực, thường được dùng cho sự kiện trực tiếp như thể thao, âm nhạc, và tin tức.

Trong khi đó, on-demand streaming giúp người dùng truy cập thư viện nội dung như các bộ phim bất kỳ lúc nào (không cần phải theo lịch phát sóng).

Adaptive bitrate (ABR) streaming

Adaptive bitrate (ABR) streaming (tạm dịch là “truyền phát video tương thích tốc độ bit” hay “bitrate thích ứng”) là một thuật ngữ chỉ một kỹ thuật (công nghệ) truyền phát video. Đơn giản ABR thực hiện trên nguyên tắc theo dõi và phát hiện (detect) khả năng của client mà chủ yếu là băng thông của user (user’s bandwidth) theo thời gian để lựa chọn phiên bản video với bitrate phù hợp đã được mã hóa sẵn từ một video gốc (single media source).

Các biến thể (variants, tức các renditions) thường có độ phân giải và chất lượng khác nhau để có bitrate phù hợp với điều kiện mạng. Trong quá trình streaming, thuật toán ABR sẽ tự động điều chỉnh chất lượng video ví dụ khi băng thông thay đổi bất thường (fluctuate) bằng cách chuyển đổi qua lại (switch) giữa các renditions. Ví dụ, nếu kết nối Internet chậm, ABR player sẽ chọn rendition có bitrate thấp để tránh giật, lag. Mặc dù các yếu tố như khả năng xử lý của CPU hay codec nào được hỗ trợ cũng có thể ảnh hưởng đến việc chọn rendition, nhưng bitrate vẫn là yếu tố quan trọng nhất. Các loại ABR algorithm có thể kể gồm có throughput-based algorithms, buffer-based algorithms và loại kết hợp nhiều thông tin (hybrid algorithms).

Xem thêm

What is adaptive bitrate streaming? | Cloudflare

Adaptive Bitrate Streaming: How It Works and Why It Matters | Wowza

Progressive download

Nội dung VOD có thể phân phối đến người dùng thông qua progressive download hay chính xác hơn là HTTP progressive download. Thay vì phải đợi toàn bộ nội dung (toàn bộ tập tin) được tải xong hoàn toàn, phương thức này cho phép người dùng bắt đầu xem video khi một phần nội dung được tải xuống.

Video cũng sẽ được tải về từng phần và lưu trên thiết bị của người dùng dưới dạng tập tin.

Lưu trực tiếp trên thiết bị lưu trữ (như ổ cứng), ví dụ tại thư mục tạm (temporary directory) của trình duyệt.

Khác với ABR streaming, ABR streaming dùng bộ nhớ cache (cache memory) của player.

Nội dung video được tải xuống tuyến tính, từ đầu đến cuối một cách liên tục, từng phần

Nếu người xem dừng lại giữa chừng, video vẫn tiếp tục tải cho đến khi hoàn thành.

Nếu không xem hết video, phần băng thông (dữ liệu Internet) đã tải sẽ bị lãng phí.

Nhược điểm chính là bảo mật kém

Thông tin truyền qua HTTP dễ bị capture hoặc sniff (nghe lén).

Có thể dễ dàng download toàn bộ nội dung.

Mã hóa toàn bộ tập tin là bắt buộc nếu muốn bảo vệ nội dung.

Mức độ bảo vệ nội dung cao như ABR streaming kết hợp với DRM

ABR streaming cho phép mật mã hóa từng phần và bảo vệ trong quá trình streaming.

Thao tác với tập tin lớn từ phía server ví dụ tìm kiếm đoạn dữ liệu phục vụ cho việc download sẽ tốn thời gian hơn.

Progressive download, phát triển từ những năm 1990, là một trong những cách tiếp cận đầu tiên của việc streaming. Với cơ chế đơn giản hơn so với các phương thức hiện đại như ABR streaming, progressive download còn được gọi là pseudo-streaming (tạm dịch là “giả streaming”, mặc dù không hoàn toàn chính xác). Phương pháp này cũng mở đường cho sự phát triển các công nghệ streaming sau này, đặc biệt là ABR, bắt đầu phổ biến từ cuối những năm 2000.

Dù đơn giản, progressive download vẫn rất hữu ích trong nhiều tình huống. Ví dụ, nó phù hợp khi không cần thích ứng bitrate hoặc khi cần tải nội dung để xem offline. Trong trường hợp D2G, việc tải có thể thực hiện với nhiều luồng download đồng thời (downloading threads).

Adaptive streaming protocols

Giao thức truyền phát (tức streaming video và audio) cơ bản là tập hợp tiêu chuẩn và công nghệ quy định cách thức truyền phát hình ảnh, âm thanh qua Internet. Do đặc thù hoạt động qua mạng Internet, nên các giao thức này đều là các giao thức thích ứng/thích nghi với sự thay đổi điều kiện mạng (adaptive streaming protocols).

Về bản chất, adaptive streaming và ABR streaming là hai thuật ngữ cùng đề cập một nhóm công nghệ chỉ hơi khác nhau về cách diễn giải. ABR streaming là tên gọi khác của adaptive streaming nhấn mạnh vào khả năng thích ứng với bitrate thay đổi (yếu tố quan trọng nhất), trong khi adaptive streaming bao quát khả năng thích ứng nói chung. Ngoài ra, hầu hết các giao thức streaming hiện tại là dựa trên (giao thức) HTTP gọi là HTTP-based media streaming protocols hay HTTP-based media streaming communications protocols.

Hai giao thức phổ biến nhất hiện nay là HTTP Live Streaming (HLS) do Apple phát triển và Dynamic Adaptive Streaming over HTTP (DASH hay MPEG-DASH) được đề xuất và phát triển bởi MPEG.

HLS được phát triển bởi Apple như một phần của QuickTime X và iOS. Lần đầu tiên HLS được giới thiệu là trong sự kiện ra mắt iPhone 3 vào mùa hè năm 2009.

Về cơ bản, HLS chia video thành các phân đoạn nhỏ (gọi là video chunks hay segments) và đóng gói mỗi phân đoạn vào một file MPEG2-TS.

Quá trình chia nhỏ này (còn gọi là băm hay segmenting) được thực hiện bởi một công cụ gọi là file segmenter (hay stream segmenter).

Segmenter này cũng chịu trách nhiệm sinh ra một tập tin chỉ mục (hay danh sách phát – hay playlist của các segments) kèm theo metadata mô tả codec, độ phân giải, bitrate, và các thông tin khác.

Tập tin danh sách phát (playlist file) sử dụng định dạng M3U8 format (với URL format extension là .m3u8.

Việc truyền tải các tập tin này sử dụng giao thức HTTP thông thường (nên gọi là dựa trên HTTP – HTTP-based streaming protocol).

M3U8 có lịch sử là M3U một định dạng tập tin danh sách phát (playlist file), ban đầu được sử dụng trong các phần mềm phát nhạc ví dụ như Winamp và VLC.

M3U là cách viết tắt của MP3 URL vì các phần mềm lúc này chủ yếu phát nhạc MP3 (MPEG-1/2 Audio Layer 3).

M3U8 là phiên bản mở rộng của M3U, hỗ trợ định dạng UTF-8.

Việc HLS chọn M3U8, một định dạng file text đơn giản, sẵn có, và được nhiều media player hỗ trợ, cũng giúp HLS dễ triển khai.

HLS có thể tận dụng cơ sở hạ tầng HTTP hiện hữu, sử dụng được các web server tiêu chuẩn để lưu trữ và phân phối video segment files cũng như playlist file. Việc sử dụng HTTP để truyền tải có ưu điểm dễ dàng triển khai vì HTTP là giao thức web cơ bản và phổ biến, được hỗ trợ rộng rãi trên hầu hết server và thiết bị.

Apple về sau vào tháng 5 năm 2009 đã đệ trình solution của mình lên Internet Engineering Task Force (IETF) để xem xét HLS là một Request for Comments (RFC).

Rất nhiều solution đã được phát triển dựa trên đề xuất này bao gồm cả open-source lẫn độc quyền (proprietary) từ server implementation (chủ yếu là cho segmenter) tới client tức player.

Phiên bản chính thức RFC 8216 được phát hành vào 2017-08, tương ứng phiên bản thứ 7 của HLS (các version draft trước đó có tên là draft-pantos-http-live-streaming).

Bản mới nhất của của RFC 8216 là HTTP Live Streaming 2nd phát hành 2024-11 tại draft-pantos-hls-rfc8216bis-15 (ietf.org).

HLS là giao thức độc quyền tự nhiên dành cho hệ sinh thái thiết bị của Apple. App Store Review Guidelines (section 2.5.7) yêu cầu tất cả nội dung video streaming qua mạng di động (cellular network) trên 10 phút phải dùng HLS.

DASH tức MPEG-DASH được phát triển dựa trên đề xuất của 3GPP và trở thành tiêu chuẩn quốc tế khi được phê duyệt (ratified) vào tháng 12 năm 2011. ISO/IEC công bố chính thức trong ISO/IEC 23009-1 với phiên bản đầu tiên phát hành tháng 4 năm 2012 (hiện tại là phiên bản thứ 5, ISO/IEC 23009-1:2022)

Trước thời điểm ra mắt DASH, các giao thức streaming đều là các giải pháp độc quyền (proprietary) từ một nhà cung cấp riêng lẻ (vendor-centric solutions).

Những giao thức này bao gồm HLS của Apple, Smooth Streaming của Microsoft hay HTTP Dynamic Streaming (HDS) của Adobe.

Như được mô tả trong tài liệu ISO/IEC 23009-1, DASH có thể được xem như là sự tổng hợp của ba giao thức streaming thích ứng nổi bật trong ngành – Adobe HDS, Apple HLS và Microsoft Smooth Streaming.

Mục tiêu của MPEG-DASH là một tiêu chuẩn chuẩn mở, không phụ thuộc vào nền tảng hoặc thiết bị cụ thể, hỗ trợ nhiều loại codec khác nhau (codec-agnostic).

HLS chủ yếu liên kết với hệ sinh thái công nghệ của Apple.

Smooth Streaming cũng từng được sử dụng rộng rãi nhưng đã bị Microsoft ngừng hỗ trợ vào năm 2021.

Adobe HDS được xem như một phần của Adobe Flash Player và Adobe Media Server cũng bị ngừng hỗ trợ vào năm 2020.

DASH dùng XML Media Presentation Description (MPD) là định dạng cho tập tin danh sách phát (playlist file) tương tự như cách HSL sử dụng m3u8 hay HDS sử dụng f4m.

Khi chọn giao thức streaming, có nhiều ràng buộc và yếu tố cần xem xét.

Ví dụ, HLS yêu cầu bắt buốc dành cho hệ sinh thái của Apple.

Các yếu tố khác có thể kể là khả năng hỗ trợ container, subtitle, và codec.

Và một điều quan trọng là sự tương thích với DRM khi ba công nghệ DRM chính là Widevine của Google, FairPlay của Apple, và PlayReady của Microsoft cũng có những yêu cầu và hạn chế riêng, và không hoàn toàn tương thích với nhau.

Tham khảo tài liệu kỹ thuật về HTTP Live Streaming (HLS) và best practice Apple HLS specs tại Apple Developer.

Xem thêm tài liệu đặc tả tại diễn đàn DASH Industry Forum | Catalyzing the adoption of MPEG-DASH (dashif.org)

Bitrate ladder

Thang bitrate (bitrate ladder, còn gọi là encoding/transcoding bitrate ladder) là thuật ngữ streaming, chỉ tập hợp các mức chất lượng video đã xác định sẵn (pre-defined video quality levels) để thuật toán ABR lựa chọn.

Cụ thể, bitrate ladder thường bao gồm ba thông tin chính:

Bitrate, tốc độ bit tức lượng dữ liệu hay lưu lượng dữ liệu sẽ sử dụng.

Độ phân giải (resolution) hay chính là kích thước khung hình tính theo pixel (ví dụ: 360p, 720p, 1080p, 4K)

và tốc độ khung hình (frame rate), lượng khung hình hiển thị mỗi giây

Nếu thông tin tốc độ khung hình không quan trọng (như nhau) thì bitrate ladder có thể chỉ gồm 2 thông tin bitrate và độ phân giải.

Thang bitrate thường được sắp xếp theo thứ tự từ cao xuống thấp.

Bậc trên cùng (top rung) là luồng video với bitrate cao, độ phân giải cao và tốc độ khung hình cao, dành cho người xem với mạng nhanh, ổn định và thiết bị công nghệ tiên tiến.

Các bậc bên dưới sẽ cung cấp các mức chất lượng thấp hơn cho người dùng với điều kiện mạng và thiết bị hạn chế.

Ví dụ một bitrate ladder đơn giản 5 mức (simple 5-rung encoding bitrate ladder) trích 1 phần của Apple’s H.264 ladder (mục 1.25, Apple HLS specs) sẽ được mô tả dạng như sau:

Table 2-5: Ví dụ bitrate ladder

Chunk hay chunking

Với ABR streaming, video hoặc âm thanh được chia thành các đoạn nhỏ, gọi là chunk hay segment. Các đoạn này thường có độ dài từ 2 đến 10 giây (được gọi là chunk length hay chunk size), và được mã hóa cũng như lưu trữ độc lập. Việc chia video thành các chunk giúp dễ dàng quản lý và truyền tải nội dung theo từng phần, thay vì phải truyền tải toàn bộ video một lần.

Chunking là quá trình mã hóa video gốc với nhiều bitrate khác nhau và chia video thành chuỗi các chunk có kích thước đồng đều, không chồng lấp nhau (non-overlapping). Nó còn được biết với tên là chunked encoding hay segmenting. Mỗi chunk phải chứa ít nhất một I-frame (khung hình chính, xem phần [2.3.9 — I-frame (video)]). Điều này đảm bảo rằng trình phát video có đủ thông tin để bắt đầu phát từ bất kỳ đoạn nào mà không cần phụ thuộc vào các đoạn trước đó.

Sau khi video được chia thành các chunk, chúng cần được đóng gói vào các tập tin riêng biệt có định dạng phù hợp hỗ trợ streaming. Các chunk được thường “đóng gói” (packaging) vào các tập tin có định dạng như TS hay fragmented MP4 tùy thuộc giao thức sử dụng như HLS hoặc DASH (xem [2.3.16 — Adaptive streaming protocols]).

Quá trình packaging cũng tạo ra một “tập tin chỉ mục” (index file), thường được gọi là “manifest file” (tạm dịch “tập tin kê khai”). Manifest file có vai trò rất quan trọng, bao gồm các thông tin sau:

Chứa nhiều danh sách phát (playlist file), mỗi danh sách phát sẽ tương ứng với một rendition (xem [2.3.12 — Renditions]), tức một phiên bản chất lượng hay một bậc của bitrate ladder.

Các danh sách phát đi kèm các thông tin như bitrate, codecs, độ phân giải, giúp trình phát (player) lựa chọn nội dung phù hợp với điều kiện mạng.

Mỗi danh sách phát sẽ chứa toàn bộ thông tin về các phân đoạn nội dung.

Là một danh sách tham chiếu đến các tập tin đã được đóng gói của chunk/segment.

Cung cấp thông tin về vị trí và thứ tự của các chunk/segment, giúp trình phát tải và phát nội dung một cách liên tục.

Đồng thời hỗ trợ khả năng phát lại từ một vị trí cụ thể của video on-demand hay cả live có ghi lại (recorded live).

Đầu tiên, client sẽ tải về manifest file.

Manifest file mô tả tất cả các chunk/segment cùng với các thông số liên quan, như các bitrate (bitrate ladder) dành cho ABR streaming.

Khi bắt đầu phát, client thường sẽ yêu cầu tải chunk/segment từ stream có bitrate thấp nhất (bắt đầu chậm).

Nếu client phát hiện ra rằng thông lượng mạng (network throughput) hiện tại cao hơn bitrate của chunk/segment đang phát, nó sẽ yêu cầu các chunk/segment từ stream có bitrate cao hơn và ngược lại, nếu thông lượng giảm.

Fragmented MP4 (fMP4)

MP4 (tên ngắn gọn của MPEG-4 Part 14) là một container format được tiêu chuẩn hóa ISO/IEC tại   ISO/IEC 14496-12 (lần đầu tiên vào năm 2004, phiên bản hiện tại là ISO/IEC 14496-12:2022).

Nó được xây dựng trên cở sở ISO Base Media File Format (ISOBMFF hay ISO-BMFF) hay còn gọi là MPEG-4 Part 12.

Bản thân MPEG-4 Part 12 lại được phát triển dựa trên Apple’s QuickTime container (file) format. MP4 ban đầu được phát triển để lưu trữ và phân phối các file multimedia, (video và âm thanh) cho các ứng dụng và thiết bị không yêu cầu phát trực tiếp qua mạng (tức chỉ tập trung cho local playback).

Các thiết bị phát media di dộng (portable media players) chơi được file MP4 những năm 2005-2007 kiểu Sony Walkman, iPod Video, iPod Touch (tức có màn hình) còn được gọi hay quảng cáo là thiết bị MP4 (MP4 players).

Tham khảo file format của MP4 tại MP4 File Format (fileformat.com)

Xem thêm ISO BMFF Byte Stream Format (w3.org)

Figure 2-1: MPEG-4 Part 14 extends over ISO Base Media File Format (MPEG-4 Part 12) — Wikipedia

Với MP4 truyền thống (traditional MP4), player cần phải tải về toàn bộ file hoặc ít nhất cũng phải chờ khá lâu để chuẩn bị đủ dữ liệu đệm (sufficiently buffered, ví dụ với HTTP progressive download hay còn gọi là HTTP pseudo-streaming) trước khi phát.

Nguyên nhân trong cấu trúc của MP4, dữ liệu metadata (hay còn gọi là “moov” box) vốn chứa thông tin cần thiết để có thể playback lại nằm riêng biệt với dữ liệu video (hay media data “mdat” box). Khối “moov” box này thông thường được đặt ở cuối tập tin do đó player phải tải hết file còn không server cần phải quét để xác định vị trí của “moov” box để trả dữ liệu cho client.

Hơn nữa metadata của file MP4 (non-fragmented) khá nặng (heavy metadata) làm cho nó không hiệu quả khi streaming. Không phải server nào cũng hỗ trợ HTTP progressive download/HTTP pseudo-streaming.

Một trong những cách để tối ưu hóa cho progressive download là di chuyển “moov” box lên đầu file. Việc này có thể thực hiện ví dụ bằng cách dùng -movflags +faststart với FFmpeg.

GitHub - danielyaa5/qtfaststart2: A smarter and more reliable version of FFMPEG's qt-faststart

Fragmented MP4 (fMP4) là một phiên bản cải tiến của tiêu chuẩn MP4, được thiết kế cho mục đích streaming qua Internet.

Nó có thể chia MP4 truyền thống (original MP4) thành các đoạn nhỏ hơn nữa, độc lập và có thể giải mã ngay.

Nhờ đó, video có thể phát ngay sau khi tải xong một phân đoạn đầu, cải thiện trải nghiệm streaming trên các mạng có tốc độ khác nhau.

Khác biệt chính của original MP4 và fragmented MP4 (fMP4) là về cách chia nhỏ và tổ chức dữ liệu:

Original MP4 — Dữ liệu video và âm thanh (media), metadata … được mã hóa và lưu trữ trong các box (hay còn gọi là atom) khác nhau như “moov” box (movie metadata) – container for all the movie metadata, “mdat” box (media data) – data container for media ...

Fragmented MP4 (fMP4) — Sử dụng một “phân đoạn khởi tạo” (initialization segment) và chuỗi các “phân đoạn media” (media segments).

Phân đoạn khởi tạo (initialization segment) bao gồm “ftyp” box (file type, description, and the common data structures) và “moov” box, cung cấp thông tin về luồng và chỉ ra rằng nó được phân mảnh. Initialization segment cần được tải trước các phân đoạn media để chuẩn bị cho quá trình playback nên chỉ chứa những thông tin thực sự cần thiết để giảm thời gian start-up.

Các đoạn phân media (media segments) chứa “moof” box (movie fragment) là dữ liệu metadata cho đoạn đó, và “mdat” box (media data) riêng chứa dữ liệu video và âm thanh.

Minh họa cấu trúc của fragmented MP4 (fMP4) cải tiến từ MP4 như sau

Figure 2-2: Fragmented MP4 (fMP4) — Container File Formats: Definitive Guide (2023) | Bitmovin

Như vậy, với fMP4 một file lớn về cơ bản có thể cắt nhỏ thành các segments.

Một segment có thể chứa một chuỗi các đoạn movie (hay các “mảnh”, dịch từ “fragment”) liên tiếp nhau (consecutive set of movie fragments). Mỗi movie fragment sẽ bao gồm một “moof” box theo sau là một hay nhiều “mdat” box.

Một subsegment là một phần của segment, cũng chứa một tập các movie fragments liên tiếp nhau (consecutive set of movie fragments). Và cứ thế, subsegment lại có thể chia nhỏ hơn nữa cho đến khi chỉ còn một movie fragment (single movie fragment per subsegment).

Thông tin khởi tạo (initialization information) của initialization segment sẽ cần dùng để thiết lập encoder (theo phần 6.3.3 “Initialization Segment format” theo ISOBMFF, tiêu chuẩn của DASH, ISO/IEC 23009-1).

Microsoft là công ty tiên phong trong việc sử dụng định dạng fMP4 vào năm 2011 với công nghệ Smooth Streaming.

Sau đó, fMP4 đã trở thành một phần quan trọng của MPEG-DASH và trở nên phổ biến hơn nhờ sự phát triển của DASH.

Mặc dù, HLS từng được ưa chuộng vì tính tương thích, DASH hiện đang ngày càng phổ biến hơn bởi hỗ trợ hầu hết các trình duyệt và codec, cũng như DRM hiệu.

Trong khi, HLS ban đầu yêu cầu phải sử dụng MPEG-2 TS (TS), thì DASH, mặc dù hỗ trợ TS, nhưng thực tế triển khai hầu như chỉ sử dụng ISOBMFF (chính xác là các biến thể dựa trên ISOBMFF).

Điều này có nghĩa các nền tảng phát trực tuyến phải duy trì hai định dạng container khác nhau: TS cho HLS và ISOBMFF cho DASH.

Nguyên nhân chính xuất phát từ bản chất độc quyền (proprietary nature) về cơ sở hạ tầng Apple. Apple yêu cầu phải sử dụng HLS cho các thiết bị như Safari, iOS và tvOS, trong khi HLS chỉ dùng TS.

Đến năm 2016, Apple mới chính thức công bố hỗ trợ fMP4 cho HLS (fMP4 over HLS), bên cạnh định dạng TS, tại Worldwide Developer Conference (WWDC).

Việc chọn container format hay segment (container) format, phụ thuộc vào nhiều yếu tố ngoài codec video và audio còn bao gồm cách tổ chức và định dạng phụ đề (subtitles), hỗ trợ nhiều luồng âm thanh (multiple audio tracks), và quản lý quyền kỹ thuật số (DRM) … Trong đó yếu tố cực kỳ quan trọng là tính tương thích (compatibility) không chỉ với thiết bị đầu cuối mà còn với các tính năng và toàn bộ hệ thống.

Ví dụ, một số các ràng buộc của HLS (trong Apple HLS specs) liên quan fMP4 như sau:

Container format cho HEVC/H.265 video phải là fMP4 (mục 1.5). Điều này dẫn tới việc hỗ trợ HDR HEVC cũng sẽ giới hạn ở fMP4 over HLS.

Audio data phải được được cung cấp dưới dạng luồng âm thanh cơ bản (elementary audio stream) hoặc trong fMP4 (mục 2.1).

xHE-AAC, Apple Lossless, và FLAC audio phải dùng fMP4 (mục 2.25).

Phụ đề phải là WebVTT (theo đặc tả HLS) hoặc IMSC1 đóng gói trong fMP4 (mục 5.2).

CMAF (container)

Common Media Application Format (CMAF) được phát triển thông qua sự hợp tác giữa Apple và Microsoft và được đệ trình lên MPEG để chuẩn hóa vào năm 2016.

Giống như fMP4, CMAF dựa trên ISOBMFF với mục tiêu sử dụng một định dạng chung để giảm chi phí tạo nhiều bản sao nội dung giữa DASH và HLS, đồng thời giảm độ phức tạp và độ trễ.

Năm 2018, CMAF chính thức được công nhận là tiêu chuẩn trong MPEG-A Part 19 và ISO/IEC 23000-19 (phiên bản hiện tại ISO/IEC 23000-19:2024 phát hành 2024-02).

Xem thêm

Common Media Application Format with HTTP Live Streaming (HLS) | Apple Developer Documentation

What Is CMAF (Common Media Application Format) | Wowza

Common Encryption (CENC)

Encrypted Media Extensions (EME)

Manifest

Manifest (hay manifest file, có thể tạm dịch “tập tin kê khai/mô tả”) là thuật ngữ chỉ một “tập tin chỉ mục” (index file) hay “tập tin danh sách phát” (playlist file) sử dụng trong công nghệ adaptive streaming (như HLS, DASH). Manifest chứa thông tin metadata về vị trí của các phân đoạn (chunk hay segment) của video hoặc âm thanh. Tùy theo cấu hình và công nghệ thường có hai loại manifest:

Một manifest “master” chứa thông tin về vị trí của mỗi manifest phiên bản (rendition manifest)

và một manifest cho từng phiên bản, trong đó chứa vị trí (tương đối hoặc tuyệt đối) của từng chunk của nguồn video hoặc âm thanh.

Subtitles và closed captions

“Phụ đề” (subtitles) và “chú thích” (captions, hay còn gọi là “phụ đề thuyết minh”) là hai thuật ngữ khác nhau và cần phân biệt với nhau. Hai thuật ngữ này thường sử dụng như nhau và cùng được dịch chung là “phụ đề”. Dù cả “phụ đề” và “chú thích” đều hiển thị dạng văn bản trên màn hình, chúng phục vụ mục đích khác nhau và có đặc điểm riêng biệt.

Riêng với caption lại chia làm 2 loại theo tính chất “có thể đóng/mở hay không” gọi là

Open caption (chú thích mở) — Thuật ngữ được sử dụng để chỉ các phụ đề mà không thể tắt hoặc ẩn đi (còn gọi là đã được “burned-in”). Việc này để đảm bảo rằng mọi người đều có thể xem nội dung phụ đề, không phụ thuộc vào cài đặt của thiết bị.

Closed caption (CC, chú thích đóng) — Người dùng có thể bật hoặc tắt các chú thích này thông qua cài đặt trên thiết bị phát video.

Về cơ bạn subtitles và captions khác nhau ở mục đích và cả mối quan hệ của chúng với âm thanh mà chúng mô tả:

Captions — Dùng chú thích, giải thích, thuyết minh và thường dùng cùng ngôn ngữ của âm thanh. Ví dụ phim có âm thanh tiếng Anh thì captions có ngôn ngữ cũng là tiếng Anh. Đây là tính năng chủ yếu được sử dụng để hỗ trợ khả năng tiếp cận (accessibility), đặc biệt cho những người khiếm thính hoặc có khó khăn trong việc nghe (deaf or hard-of-hearing).

Captions không chỉ bao gồm văn bản của lời thoại mà còn thể hiện các âm thanh không phải lời nói (như tiếng nhạc, tiếng động, tiếng cười, hoặc các âm thanh môi trường quan trọng) để giúp người xem hiểu rõ hơn về nội dung của video mà không cần nghe.

Đây là tính năng bắt buộc với một số chương trình chủ yếu là truyền hình và được luật hóa ở nhiều quốc gia. Ví dụ điển hình là đạo luật liên bang Americans with Disabilities Act (ADA) và các quy định của FCC (Federal Communications Commission) tại Hoa Kỳ (tham khảo Closed Captioning on Television | FCC).

Subtitles — Thường phục vụ cho những người không hiểu ngôn ngữ gốc của video. Tức là bản phụ đề cho ngôn ngữ nói đã được dịch sang một ngôn ngữ khác (spoken audio translated into another language). Ngoài ra, subtitles thường chỉ thể hiện lời thoại và thường không bao gồm các âm thanh khác. Do đó, đôi khi caption còn được gọi với tên là “phụ đề nội ngữ” (intralingual subtitles) và subtitles sẽ được gọi là “phụ đề liên ngữ” (interlingual subtitles).

Trong tài liệu này khi dùng thuật ngữ “phụ đề” có nghĩa đang dùng thuật ngữ “subtittles”.

Lưu ý rằng các quy định phát sinh (nếu có sau này) về closed captions (CC) theo yêu cầu từ cơ quan quản lý nhà nước, sẽ được cập nhật vào tài liệu.

Có nhiều khái niệm dùng để phân chia loại phụ đề, tuy nhiên các khái niệm thường dùng để phân chia đầu tiên là quan hệ giữa phụ đề với media stream:

Phụ đề “in-band” (in-band subtitles, tạm dịch phụ đề “trong luồng/cùng luồng”) — Là phụ đề (hoặc text tracks nói chung, văn bản liên quan đến video hoặc âm thanh) được nhúng trực tiếp vào media stream. Điều này có nghĩa phụ đề sẽ sẽ được phát cùng với nội dung media (in-band có nghĩa cùng một phương thức – same method, cùng một đường – same path, cùng một kênh truyền – same channel). Phụ đề “in-band” còn có tên gọi khác là “phụ đề stream” (stream subtitles hay in-stream subtitles) hay phụ đề nhúng (embedded subtitles) tức chỉ cụ thể hơn là phụ đề được nhúng trực tiếp vào tập tin video/audio.

Lưu ý phụ đề nhúng (embedded subtitles) vẫn có thể bật/tắt được và không phải thuật ngữ chỉ phụ đề cứng được chèn vào video gọi là “burn-in subtitles” hay “in-vision subtitles”.

Luôn đồng bộ với video vì chúng vì được phân phối cùng với nội dung video.

Định dạng chính của loại (primary format for in-band) này là CEA-608/CEA-708 (xem ví dụ CEA 608/708 Embedded Captions Sample | dashif.org). Nó cũng có thể là loại IMSC1 được nhúng vào file ISOBMFF theo tiêu chuẩn MPEG- 4 Part 30 “Timed Text and other Visual Overlays in ISO base Media File Format” (ISO/IEC 14496-30).

Phụ đề “out-of-band” (out-of-band subtitles, tạm dịch phụ đề “ngoài luồng/khác luồng”) — Đây là loại phụ đề khác với “in-band” subtitles, không nằm trong media stream.

Có thể dễ dàng thêm, cập nhật, hoặc xóa phụ đề mà không cần thay đổi media stream.

Có thể linh hoạt hỗ trợ nhiều ngôn ngữ hoặc kiểu phụ đề khác nhau, cũng như có thể dễ dàng tích hợp các tính năng như AI để dịch tự động.

Phụ đề “out-of-band” chỉ mang ý nghĩa là được phân phối qua một kênh riêng không phải là nhúng trong media stream. Tuy nhiên, phụ đề này thường được tham chiếu và liên kết với media thông qua tập tin manifest.

Các thuật ngữ khác về liên quan tới quan hệ giữa phụ đề và manifest:

Phụ đề “sidecar” (sidecar subtitles) tức phụ đề rời và đi kèm — Đây là một tập tin riêng biệt, dạng văn bản (separated subtitle text file) chứa phụ đề cho toàn bộ thời gian của video/audio, thường ở định dạng WebVTT (giống với SRT) hoặc TTML (hoặc biến thể của nó như IMSC).

Phụ đề “sidecar” thường không nằm trong manifest của video (tức “tập tin chỉ mục” hay “tập tin danh sách phát”). Điều này cũng có nghĩa phụ đề “sidecar” hiển nhiên là một loại phụ đề “out-of-band”. Hệ thống thường sẽ cung cấp thông tin về tập tin chứa phụ đề “sidecar” thông qua API.

Tên gọi “sidecar” xuất phát từ việc tập tin phụ đề được lưu trữ cạnh tập tin video trong lịch sử. Nó chỉ ra rằng phụ đề được chuẩn bị và lưu trữ cùng với nội dung video/audio, chẳng hạn như trong cùng một thư mục hoặc bucket. Tên tập tin phụ đề thường khớp với tên video, theo định dạng “[movie-file-name].[language-code].extension” (với language code thường theo ISO-639-1/ISO-639-2), giúp player tự động nhận diện và hiển thị phụ đề.

Phụ đề “sidecar” còn được biết với tên là phụ đề “tải bên ngoài” (side-loaded subtitles) hay đơn giản là phụ đề “bên ngoài” (external subtitles) tức là phụ đề nằm trong một tập tin riêng biệt và player phải thực hiện tải và thiết lập thủ công (thông qua settings hoặc code).

Phụ đề tham chiếu trong manifest (in-manifest subtitles hay in-manifest referenced) — Phụ đề được tham chiếu và quản lý thông qua tập tin manifest.

Như phân loại ở trên thì phụ đề “in-manifest” cũng là loại phụ đề “out-of-band” vì không nằm trong media tream.

Được gắn với/ghép vào (stitched) tập tin manifest của video, ví dụ trong HLS m3u8 manifest với chỉ thị EXT-X-MEDIA:TYPE=SUBTITLES.

Được quy định rõ ràng theo giao thức streaming như HLS hoặc DASH, giúp việc tích hợp và hiển thị phụ đề trở nên nhất quán và dễ dàng. Do đó loại phụ đề này thường được hỗ trợ phổ biến hơn trên các player tại đầu cuối (endpoint players).

Ngoài ra, phụ đề có thể được phân chia theo tính chất “có bị phân mảnh hay không” (fragmented hay non-fragmented).

Loại đầu tiên là phụ đề “bị phân mảnh” (fragmented/segmented subtiles) — Ví dụ subtitle là loại “in-stream subtiles” như với fMP4 HLS/DASH streams thì nó sẽ là loại “fragmented in-stream subtiles”. Đây là định dạng mà phụ đề cũng được phân chia thành các phân đoạn, như cách phân chia media stream. Ví dụ WebVTT dạng raw có thể embedded trong fMP4 (ISO/IEC 14496-30).

Phụ đề “không bị phân mảnh” (non-fragmented subtiles) — Khác với loại bị phân mảnh thì đây là loại chứa phụ đề cho toàn bộ thời gian của video/audio, không được chia thành các đoạn nhỏ. Tất nhiên, phụ đề “không bị phân mảnh” vẫn có thể chia làm 2 loại là in-band (hay non-fragmented in-stream subtitles) hay out-of-band.

Thumbnail preview (feature)

Tính năng xem trước bằng hình ảnh thu nhỏ (thumbnail preview hay timeline hover preview) cho người dùng xem hình ảnh nhỏ đại diện cho khung hình của video ở thời điểm mà không cần phải nhấn play hay tua tới thời điểm đó. Người dùng chỉ cần di chuyển chuột trên thanh trượt của player (timeline bar, seek bar hay scrub bar) thể hiện dòng thời gian của video (progress timeline).

Do tính chất tương đồng với subtitle, tính năng này thường sử dụng WebVTT (Web Video Text Tracks) để cung cấp các hình ảnh xem trước (preview thumbnails) tương ứng với thời gian trong video.

DASH-IF IOP specification (version 5 tại thời điểm hiện tại) đã bổ sung tính năng này (từ DASH-IF IOP version 4.3) với tên “Thumbnail tracks”, dạng in-manifest với EssentialProperty tag. Tương tự, HLS tính năng này có thể implement thông qua EXT-X-I-FRAME-STREAM-INF tag (mục 4.3.4.3) hỗ trợ cả I-frame và image-based, gọi là “trick-play” hay “trick mode”.

Tuy vậy, các player vẫn thường ưu tiên sử dụng WebVTT dạng side-loaded vì tính linh hoạt và phổ biến của nó.

Xem thêm

Thumbnail Preview Support (bitmovin.com)

THEOplayer Demo - Preview Thumbnails

Working with trick-play in AWS Elemental MediaPackage - AWS Elemental MediaPackage (amazon.com)

Thumbnails thường được ghép lại thành một tấm ảnh lớn dưới dạng lưới, gọi là “mosaic” (còn được gọi là lát gạch – “tiled”). Những tấm ảnh lớn này được gọi là thumbnail sprites hoặc sprite sheets. Đây là một kỹ thuật thông dụng để giảm số lượng yêu cầu (số lượng request) và rút ngắn thời gian tải.

Việc triển khai thông qua một URL cho phép player tải tập tin WebVTT:

URL của WebVTT dạng “/media/vtt/thumbnails/{PLAYBACK-ID}-thumbnails.vtt”

WebVTT chứa danh sách các cues, mỗi cue bao gồm khoảng thời gian (time-range) dạng WebVTT timestamp (ví dụ khoảng 10 giây) và địa chỉ của thumbnail cho time-range này.

Địa chỉ của thumbnail có thể là tham chiếu đến một ảnh rời (URI tới một ảnh thumbnail) hoặc tham chiếu đến sprite sheet và thông tin tọa độ với định dạng spatial media fragment (xywh) tức thông tin tọa độ (x, y) và kích thước thumbnail (w × h)

Ví dụ nội dung WebVTT

WEBVTT

Img 1

00:00.000 --> 00:10.000

assets//{PLAYBACK-ID}-sprite-01.jpg#xywh=0,0,320,180

Img 2

00:10.000 --> 00:20.000

assets//{PLAYBACK-ID}-sprite-01.jpg#xywh=320,0,320,180

Chapter markers & cues/cue points

Các “điểm đánh dấu chương” (chapter markers) là các điểm đánh dấu (visible markers with a title or label) trên thanh tiến trình của player (progress timeline bar) phân chia một video dài thành các đoạn riêng biệt, giúp người xem dễ dàng nhảy đến các phần khác nhau, tương tự như các chương trong một cuốn sách.

Chapter markers tập trung vào khả năng điều hướng, giúp người xem dễ dàng di chuyển giữa các phần của video.

Ví dụ trong một bộ phim dài (long-form videos), có thể có các chapter markers đánh dấu cho các phân đoạn “Giới thiệu”, “Cao trào”, “Kết thúc”, giúp người xem dễ dàng điều hướng mà không cần tua thủ công.

Đặc biệt chapter markers hoàn toàn phù hợp để sử dụng cho audio book.

Về nguyên tắc, chapter marker chỉ cần thông tin về thời gian bắt đầu, thời gian kết thúc và một tiêu đề cho mỗi đoạn video.

Xem ví dụ chapter marker tại

YouTube Video Chapters - YouTube Help (google.com)

THEOPlayer What are chapter markers? | THEOdocs (theoplayer.com)

JWP Add chapter markers (jwplayer.com)

Figure 2-6: Chapter markers với title render trên UI (video canvas) — THEOplayer

File WebVTT sẽ có dạng như sau:

WEBVTT

Chapter 1

00:00:00.000 --> 00:01:42.000

Opening credits

Chapter 2

00:01:42.000 --> 00:04:44.000

A dangerous quest

Chapter 3

00:04:44.000 --> 00:05:50.000

The attack

Tính năng thumbnail preview (feature) hoàn toàn có thể kết hợp với chapter marker, vì cung cấp thông tin bằng hình ảnh (thumbnail) trong khi chapter marker chủ yếu cung cấp thông tin văn bản (tiêu đề chương).

Ngoài ra, chapter marker cũng thường sử dụng trong tính năng playlist cho phép user có thể nhanh chóng chuyển bài.

Figure 2-7: Sử dụng chapter markers cho playlist — YouTube

Các “điểm (đánh dấu) gợi ý” (visual-cue points, visual cues hay time marker) là cũng là các điểm đánh dấu (visible markers) trên thanh tiến trình của player (progress timeline bar) nhưng thường dùng để đánh dấu thời điểm chính xác (precise time point) thay vì một khoảng thời gian dài (duration) như chapter markers.

Cue points thường dùng để đánh dấu sự kiện

Ví dụ, nó có thể được sử dụng để chỉ thời điểm sẽ có mid-roll ads (quảng cáo giữa video) hay sẽ kích hoạt sự kiện đặc biệt.

Do đó, cue point chỉ cần một thông tin về thời gian là timecode (hh:mm:ss) cùng với các dữ liệu bổ sung như thumbnail, tiêu đề (title) và mô tả (description).

Không chỉ được sử dụng để đánh dấu sự kiện bằng hình ảnh trực quan, cue points còn có thể xác định các điểm mà người dùng có thể tương tác.

Khi đó, cue points cần một kích thước nhất định để nhận tương tác.

Trong trường hợp này, cue points không chỉ là một điểm thời gian đơn lẻ dạng mà cần có một vùng tương tác nhỏ nhất định, chẳng hạn như 10 giây (time-range xác định bằng start time và end time), để đảm bảo khả năng tương tác của người dùng.

Tóm lại:

Chapter markers là một dạng đặc biệt của cue points dùng để đánh dấu chương.

Cả chapter markers và cue points, giống như thumbnail preview, đều có thể triển khai bằng WebVTT.

Thông tin hiển thị gồm có mốc thời gian kèm tiêu đề, mô tả, và hình ảnh.

Xem thêm thông tin về WebVTT tại

Web Video Text Tracks Format (WebVTT) - Web APIs | MDN (mozilla.org)

WebVTT: The Web Video Text Tracks Format (w3.org)

Live caption và live transcript

Chi tiết bổ sung trong release sau của đặc tả.

Time-shiting (features)

Các tính năng “time-shiting” (time-shifting features hay time-shifted viewing features, tạm dịch các tính năng xem “dịch chuyển thời gian”) là nhóm các tính năng cho phép người dùng kiểm soát hay chọn xem các chương trình trực tiếp (live) hoặc đã từng phát trực tiếp, từ một thời điểm cụ thể thay vì phải xem ngay thời điểm hiện tại.

Nhóm các tính năng time-shifting có sự tương đồng với nhau vì đều liên quan đến khái niệm “dịch chuyển thời gian” nhưng lại có nhiều biến thể cùng tên gọi khác nhau, bao gồm:

Start-over — Xem từ đầu một sự kiện đang phát sóng trực tiếp (live event), ngay cả khi sự kiện đó đã bắt đầu trước thời điểm người dùng bắt đầu xem. Có nghĩa là user có thể “quay ngược thời gian” để bắt đầu xem vào thời điểm sự kiện bắt đầu. Nếu sự kiện đã kết thúc, tính năng start-over cũng không còn có thể truy cập. User cũng không thể bắt đầu xem từ một thời điểm cụ thể khác trong quá khứ ngoại trừ thời điểm bắt đầu.

Catch-up TV (CUTV) — Xem lại các chương trình hoặc sự kiện đã được phát sóng trước đó. Điều này có nghĩa là sự kiện hoặc chương trình đã được phát sóng trực tiếp và không còn đang diễn ra. Catch-up TV thường bị giới hạn chỉ xem được trong một khoảng thời gian nhất định sau khi chương trình kết thúc ví dụ 24h hay 48h.

Mặc dù, CUTV rất giống với VOD (có thể chung nhau về công nghệ) nhưng chúng khác nhau ở cách thức truy cập, chủ yếu liên quan đến yếu tố kinh doanh (business).

CUTV mang tính chất “tái phát sóng” trong khoảng thời gian cụ thể, trong khi VOD là nội dung có sẵn lâu dài. f

Ngoài ra, CUTV thường được cung cấp dựa trên chương trình hoặc sự kiện cụ thể.

Sau khi chọn chương trình, tùy thuộc vào yêu cầu kinh doanh hoặc chính sách của dịch vụ, user sẽ có khả năng playback đầy đủ hoặc bị hạn chế một phần.

User có thể không được hỗ trợ seek (di chuyển đến thời điểm cụ thể) hay pause/resume.

Ví dụ, nếu chương trình có quảng cáo, quy định kinh doanh có thể không cho phép người dùng tua nhanh để bỏ qua quảng cáo.

Time-shifted TV — Tính năng cho phép tạm dừng và tiếp tục phát (pause and resume) truyền hình trực tiếp tức cho phép pause/resume với kênh truyền hình (linear TV, live broadcasts).

Time-shifted TV không bị ràng buộc bởi khái niệm chương trình (program). Mặc dù vẫn có lịch phát sóng (EPG), nhưng time-shifted TV không bị ràng buộc bởi ranh giới của các chương trình.

Do các kênh truyền hình phát sóng liên tục 24/7, nên pause/resume gần như đồng nghĩa với việc user có thể bắt đầu xem từ bất kỳ thời điểm nào trong quá trình phát sóng, miễn là hệ thống đã lưu trữ nội dung. Vì vậy, time-shifted TV thường hỗ trợ đầy đủ khả năng playback (full playback controls), bao gồm cả khả năng seek (tua đến thời điểm mong muốn).

Điều này khác với start-over vốn chỉ cho phép user xem lại chương trình từ đầu với điều kiện chương trình đó vẫn đang được phát trực tiếp.

In-stream ads

Có hai cách phổ biến để tích hợp nội dung quảng cáo (media advertisements) vào một ứng dụng:

In-stream ads — Quảng cáo được phát ngay trong ngữ cảnh của luồng nội dung video (hoặc âm thanh) mà người dùng đang xem.

Tức nó gắn liền với nội dung xem và ở trong cùng với trình phát video (hoặc âm thanh) mà người dùng đang sử dụng.

In-stream ads có thể xuất hiện trước (pre-roll), giữa (mid-roll), hoặc sau (post-roll) nội dung video. Người xem sẽ phải xem (hoặc nghe với trường hợp audio) hoặc bỏ qua quảng cáo (nếu được) để tiếp tục xem nội dung chính.

Outstream ads — Là loại quảng cáo không phải in-stream ads hay nói cách khác là các quảng cáo video (hoặc) đứng một mình và được đặt một cách tự nhiên trong các phần khác của ứng dụng.

Vì không cần không yêu cầu nội dung chính để đi chung nên outstream ads cũng không cần trình phát video/audio (tức media player) để xuất hiện trong ứng dụng.

Outstream ads do đó cũng không nhất thiết phải có định dạng là video (hay audio) và cũng linh hoạt hơn về vị trí sắp đặt (placement).

Với ngữ cảnh video streaming, chúng ta chỉ cần tập trung vào in-stream ads. Cụ thể có hai phương pháp chính để chèn quảng cáo (ad insertion) vào phiên xem (playback session) của người dùng là Client-Side Ad Insertion (CSAI) và Server-Side Ad Insertion (SSAI).

Xem thêm Inventory formats - Google Ad Manager Help

In-band events (ads)

Timed events (hay chính xác hơn media timed events), tạm dịch là “sự kiện hẹn giờ” (hay “sự kiện định thời”), là sự kiện được lập lịch để kích hoạt vào một thời điểm định trước. Nó liên kết với một thời điểm (point in time) hoặc một khoảng thời gian (period of time) cụ thể, và được đồng bộ với dòng thời gian của video hoặc audio (hay media timeline nói chung).

In-band events, tương tự các thuật ngữ “in-band” khác, là thuật ngữ chỉ media timed event được chèn/nhúng trực tiếp vào trong luồng video hoặc audio (media stream) mà người dùng đang xem hoặc nghe. Dữ liệu của in-band events có thể được truyền tải trong cùng container của video, hoặc được “ghép kênh” cùng media stream (muxed/multiplexed, xem [2.3.7 — Muxing (multiplexing)]).

In-band events thường được sử dụng trong các trường hợp sau:

Điều khiển chương trình và phân phối nội dung (program and distribution control), chẳng hạn như giữa nhà cung cấp nội dung và nhà phân phối để thực hiện các quy định và chính sách liên quan đến việc phát sóng, ví dụ như tình huống cần chắn sóng (blackouts).

Dùng báo hiệu (signaling) như đặc biệt là báo hiệu quảng cáo (ad break), hay báo hiệu để chuyển luồng (switching stream) sang nội dung thay thế (alternate content).

Ngược lại, out-of-band events là thuật ngữ chỉ sự kiện được truyền tải qua một cơ chế khác bên ngoài media container hoặc media stream.

Ad replacement & ad insertion (ads)

Thay thế quảng cáo (ad replacement) là việc thay thế một khoảng thời gian của chương trình mà không làm thay đổi tổng thời gian nội dung, và phương pháp này có thể áp dụng cho cả chương trình trực tiếp (live) lẫn VOD. Ngược lại, chèn quảng cáo (ad insertion) sẽ kéo dài tổng thời gian nội dung và chỉ có thể áp dụng cho VOD.

Thay thế quảng cáo khác với chèn quảng cáo rất rõ ràng, minh họa như trong sơ đồ dưới đây:

Figure 2-8: Ad replacement vs. ad insertion

Với phát sóng trực tiếp (broadcast live), nhà đài gần như biết trước chính xác lúc nào sẽ phát quảng cáo (theo kịch bản đã chuẩn bị). Quảng cáo trong phát sóng trực tiếp thường có thời lượng cố định, chẳng hạn như 2 hoặc 3 phút cho mỗi ad break. Ví dụ nếu cần phát 3 phút quảng cáo, hệ thống sẽ đảm bảo có đủ nội dung để phát đủ 3 phút mà không tạo ra khoảng trống.

Với việc thay thế toàn bộ ad break bằng quảng cáo có thời lượng tương đương với ad break là một thách thức. Để giải quyết vấn đề này, các hệ thống thường áp dụng các biện pháp sau:

Sử dụng ad pods là một nhóm các quảng cáo được phát liên tiếp nhau trong một lần thay thế ad break. Ad pods giúp lấp đầy thời lượng ad break (ad break duration) hiệu quả hơn so với việc chỉ phát một quảng cáo (một ad creative).

Fill slate còn gọi là slate ad (video đệm) sẽ được dùng để lấp đầy phần thời gian còn lại của ad break nếu quảng cáo không đủ dài.

Figure 2-9: Ad replacement with live streaming

Ad stitching (ads)

Ad stitching (hay còn gọi là splicing, tạm dịch “ghép quảng cáo”) là quá trình lấy hai hay nhiều nội dung video và kết hợp (combining), nối lại với nhau (concatenating) theo một trình tự thời gian cụ thể (timeline) để tạo thành một video mới. Ad stitching cũng là một phương pháp phổ biến để chèn hay thay thế quảng cáo phía server vào tập tin video hay chính xác hơn là vào video manifest ngay khi video đang được truyền phát đến người xem (on-the-fly, tức không phải được chuẩn bị sẵn trước đó).

SCTE-35 markers/tags

Các workflow thực hiện ad stitching thường sử dụng các “tiêu chuẩn đánh dấu/báo hiệu” (signaling standard) để mô tả các “điểm ngắt quảng cáo” (ad breaks) ngay trong luồng video. Ad breaks, còn gọi là các “điểm ghép” (splice points), là thông tin về nơi có thể thực hiện chèn hay thay thế quảng cáo. Thông tin về các ad breaks này chính là các in-band timed events, gọi là ad markers, ad tags hay ad cue points, tạm dịch là “tín hiệu đánh dấu quảng cáo”.

Trong lĩnh vực video streaming, SCTE markers/tags (đọc là “scutty”) là tên chung của các tiêu chuẩn đánh dấu (signaling standards) đang được sử dụng phổ biến nhất hiện nay. Đây là những tiêu chuẩn do Hiệp hội Kỹ sư Viễn thông (và) Cáp (Society of Cable Telecommunications Engineers – SCTE) phát triển.

Tên ban đầu của SCTE (thành lập năm 1969) là Hiệp hội Kỹ sư Truyền hình cáp (The Society of Cable Television Engineers).

Hai tiêu chuẩn quan trọng nhất trong số đó là:

SCTE-35 — Tên đầy đủ là “Digital Program Insertion Cueing Message for Cable”, được sử dụng để đánh dấu quảng cáo hoặc sự kiện trong luồng video, cho phép chèn hoặc thay thế nội dung.

SCTE-104 — Là tiêu chuẩn hỗ trợ cho SCTE-35, định nghĩa API để gửi và chèn các tín hiệu SCTE-35 vào luồng video. Nó có tên là “Automation System to Compression System Communications API”.

Ban đầu, các tiêu chuẩn này được phát triển cho truyền hình cáp, ví dụ tên của SCTE-35 có ghi rõ là “for Cable”. Tuy nhiên, sau đó chúng đã được mở rộng và được chứng minh là hữu ích và linh hoạt cho cả OTT workflows và các dịch vụ streaming hiện đại.

SCTE-35 sẽ mang lại nhiều lợi ích nhiều hơn khi sử dụng cho live streaming. SCTE-35 markers thường chỉ dùng để đánh dấu mid-roll cho nội dung VOD. Với VOD, việc sử dụng out-of-band signaling vẫn là giải pháp đơn giản và linh hoạt.

Quy trình thực hiện cụ thể với môi trường phát sóng trực tiếp (live broadcast) sẽ như sau:

SCTE-104 được sử dụng kết hợp với SCTE-35, hoạt động như một API để hệ thống chèn các SCTE-35 markers.

SCTE-104 markers gọi là các baseband markers sẽ được chèn vào luồng video gốc (video feed như luồng SDI hoặc luồng IP).

Video feed sau khi qua encoder sẽ được mã hóa thành luồng MPEG-TS. Trong quá trình này SCTE-104 markers cũng sẽ được chuyển thành SCTE-35 markers. Kết quả là luồng output MPEG-TS sẽ bao gồm SCTE-35 markers (carried in-band), cho phép các hệ thống và thiết bị downstream xử lý tiếp.

SCTE-35 có thể triển khai với HLS và DASH như sau:

Với HLS, SCTE-35 được nhúng trực tiếp vào manifest m3u8, với ba loại tags chính là #EXT-X-DATERANGE, #EXT-OATCLS-SCTE35 và #EXT-X-CUE-OUT/EXT-X-CUE-IN

Tag #EXT-X-DATERANGE là tag chính thức được hỗ trợ bởi HLS (mục 4.4.5.1)

Tag #EXT-OATCLS-SCTE35 được xem là tag nâng cao không có trong Apple HLS specs. Tuy nhiên, nó được sử dụng rộng rãi vì có thể nhúng toàn bộ data của SCTE35 dạng base64 vào manifest giúp thuận tiện trong việc xử lý.

Tag #EXT-X-CUE-OUT/EXT-X-CUE-IN đơn giản đánh dấu điểm bắt đầu (splice start point), thời lượng (duration) và điểm kết thúc (splice end point). Các tags này cũng không có trong Apple HLS specs và được xem là tag thử nghiệm (experimental tags).

Ngoài ra HSL còn sử dụng #EXT-X-DISCONTINUITY để cho biết có sự gián đoạn hay chuyển tiếp giữa nội quảng cáo và nội dung chính để player chuẩn bị, ví dụ như chuẩn bị cho thay đổi về codec (xem chi tiết tại Incorporating Ads into a Playlist | Apple Developer Documentation).

Thuật ngữ SCTE tags thường được sử dụng để chỉ SCTE markers nhất là khi sử dụng với HLS.

Với DASH, SCTE-35 tương tự cũng được khai báo trong manifest mpd, thông qua section <EventStream> với các scheme như “urn:scte:scte35:2014:xml”, “urn:scte:scte35:2014:xml+bin” hay “urn:scte:scte35:2013:xml”.

Vì DASH là tiêu chuẩn khá toàn diện và đầy đủ (comprehensive) nên việc triển khai SCTE-35 với DASH cũng được hướng dẫn khá rõ ràng và chi tiết.

Với phiên bản 5 của DASH-IF Interoperability, DASH-IF quyết định chia tài liệu đặc tả thành các phần riêng biệt, mỗi phần tập trung vào các khía cạnh cụ thể. Ad insertion là một phần lớn và quan trọng, nên được quy định trong Part 5 của DASH-IF IOP v5 (DASH-IF-IOP-Part5-v5.0.0: Ad Insertion, phát hành 2021-11).

Hai tài liệu bổ sung liên quan đến việc hướng dẫn và hỗ trợ việc triển khai là:

SCTE-67, “Recommended Practice for SCTE-35” (phiên bản hiện tại 2024), cung cấp các hướng dẫn qua các ví dụ thực tế để tối ưu hóa việc sử dụng SCTE-35.

SCTE-224, “Event Scheduling and Notification Interface (ESNI)” (phiên bản hiện tại 2021), liên quan channel scheduling, metadata và content rights (các yêu cầu về bản quyền)

Tóm lại, SCTE-35 là tiêu chuẩn cốt lõi dùng để báo hiệu, với nhiều use case đặc biệt cho việc chèn quảng cáo, cần thiết cho mọi hệ thống video streaming.

Tham khảo ví dụ

In-band SCTE-35 commands used for ad breaks | Live Stream API | Google Cloud

SSAI & DAI

Server-Side Ad Insertion (SSAI) là công nghệ chèn quảng cáo (cá nhân hóa) trực tiếp vào luồng video phía server, trước khi video được phát đến người dùng (before reaching the viewer’s device). Quảng cáo và nội dung video gốc được hợp nhất thành một luồng video duy nhất (single video stream) thông qua ad stitching, thay vì thực hiện quảng cáo phía khách hàng (client-side ad insertion – CSAI).

Người xem sẽ nhận được một luồng liên tục giữa các quảng cáo và nội dung mà không có hiện tượng khựng, trễ, dừng đột ngột để tải dữ liệu (buffering) khi chuyển tiếp.

SSAI là công nghệ yêu cầu cao về mặt hệ thống khi vừa phải thực hiện giao tiếp trên máy chủ quảng cáo và vừa phải thao tác c`hỉnh sửa manifest (manifest manipulation). Ngoài ra, hệ thống còn phải xử lý các vấn đề như manifest cá nhân hóa (personalized manifests) không thể cache được (not cacheable).

Dynamic Ad Insertion (DAI) tập trung vào chèn quảng cáo "động", lựa chọn quảng cáo phù hợp dựa trên nhiều tiêu chí và dữ liệu thời gian thực.

Định nghĩa của DAI chỉ nhấn mạnh tính “dynamic” và không hề có bất kỳ giới hạn nào về cách triển khai. Điều này có nghĩa rằng DAI rộng hơn và bao quát hơn SSAI.

SSAI là phương pháp phổ biến nhất để thực hiện DAI do những lợi thế so với CSAI như trải nghiệm liền mạch hơn, không bị chặn quảng cáo. Trong nhiều trường hợp, DAI được xem là đồng nghĩa với SSAI. Ví dụ DAI (svta.org) và SSAI (svta.org) được Streaming Video Technology Alliance (SVTA) định nghĩa không khác gì nhau.

Một số nguồn vẫn phân biệt rõ việc DAI có thể thực hiện thông qua cả SSAI hoặc CSAI, thậm chí bằng cả hybrid, ví dụ:

Bài viết trên IBC, một tổ chức lớn về công nghệ và truyền thông, “Dynamic Ad Insertion, FAST and the Future | Industry Trends | IBC” (2023-06)

Theo Broadpeak, là nhà cung cấp giải pháp, trong bài viết “Maximizing Ad Impact: The Essential Guide to Dynamic Ad Insertion and Server Side Ad Insertion | broadpeak.io” (2024-03).

Dù có nhiều lợi thế, SSAI cũng có những hạn chế, đặc biệt trong việc đo lường hiệu quả quảng cáo, phức tạp hơn so với các công cụ truyền thống như tracking pixels trong CSAI. Hơn nữa, SSAI còn gây khó khăn trong việc phân tích các chỉ số video, như xác định thời gian xem (watch time).

ĐẶC TẢ CHUNG (GENERAL SPECIFICATIONS)

Định danh và cấu hình codec (codec identifiers)

Codec identifiers (hay codec declaration) là các ký hiệu ngắn gọn để mô tả “cấu hình kỹ thuật của các codec”. Chúng được dùng trong các đặc tả codec, chẳng hạn như manifest của HLS và DASH. Tài liệu này cũng sử dụng cú pháp cơ bản (basic syntax) quy định trong RFC 6381 (và các tiêu chuẩn liên quan), để mô tả cấu hình codec một cách ngắn gọn và rõ ràng. Kiểu cơ sở hay loại cơ sở của codec (tạm dịch cho base type) là thành phần đầu tiên trong định danh codec (codec identifier) theo chuẩn RFC 6381. Nó còn có tên là fourCC string (four-character code).

Ví dụ một số video codecs thông dụng được diễn giải như sau:

H.264/AVC bắt đầu bằng chuỗi “avc1” (base type).

Có 3 profiles chính là Baseline Profile (BP), Main Profile (MP), High Profile (HP)

BP (66 = 0x42) dành cho thiết bị di động cũ (lower-cost, old mobile devices)

MP (77 = 0x4D) cho thiết bị hiện đại hơn (mainstream) hay cho web streaming

HP (100 = 0x64) dùng cho high-definition app hay broadcast.

Profile có thể kèm constraint flags (profile-iop), là cờ dùng để enable/disable tính năng (features) của encoder. Ví dụ như constrained BP (42E0), constrained MP (4D40)

Có các level từ 1 đến 5.1 thể hiện dạng hexadecimal như 30 = 0A (hexa), 42 = 2A

Tuy nhiên phổ biến là 3.0 (1E), 3.1 (1F), 4.0 (28), 4.1 (29), 4.2 (2A).

Ví dụ để tuân thủ yêu cầu của Level 4.2, nội dung video không vượt quá 2048 × 1080 @ 60 fps hay 50,000 Kbps.

Ví dụ “avc1.4d402a” được định nghĩa là “H.264/AVC Main Profile, Level 4.2” còn ghi là H.264/AVC MP @ L4.2.

HEVC/H.265 base type “hev1” hoặc “hvc1”

Profile chính của HEVC/H.265 chủ yếu là Main và Main 10

Các level thông dụng là 4.1, 4.2, 5.0 và 5.1

AV1 base type “av01”.

VP9 có base type là “vp09”.

Một số ví dụ về yêu cầu video decoding:

Google yêu cầu tất cả các thiết bị Android TV chạy Android 14 với Google TV Services (GTVS) ngoài việc tuân thủ Android 14 Compatibility Definition (CDD) phải có khả năng HD decoding cụ thể như sau

H.264 HD (1080p @ 60fps) decoding với peak bitrate 20 Mbps

VP9 HD (1080p @ 60 fps), Profile 0 decoding với peak bitrate 20 Mbps

AV1 HD (1080p @ 60 fps), Profile 4.1 decoding với peak bitrate 20 Mbps

YouTube Living Room 2023 yêu cầu thiết bị 4k (UHD) phải có khả năng

VP9 4K × 2K (3840 × 2160) @ 30/60 fps, Profile 0 (8-bit for SDR) và Profile 2 (10-bit for HDR) @ L5.1 decoding với WebM container, peak bitrate 40 Mbps.

H.264 HD (1080p @ 30/60 fps), HP @ L4.2 decoding với peak bitrate 20 Mbps với MP4 container

AV1 4K × 2K (3840 × 2160) @ 60 fps, MP @ L5.1, 8-bit SDR, 10-bit HDR decoding với MP4 container, peak bitrate 42 Mbps

Chọn lựa các thông số như profile và level là một chuyện phải cân nhắc.

Ví dụ level H.264/AVC xác định độ phân giải và tốc độ khung hình tối đa mà thiết bị hỗ trợ.

Với độ phân giải 854 × 480 (480p 16:9) hay 720 × 576 (SD), chọn HP @ L4.1 (avc1.640029) có thể không cần thiết, vì độ phân giải này không yêu cầu nhiều tính năng trừ khi muốn tối ưu hóa bitrate.

HP @ L4.1 có thể cung cấp chất lượng video tốt hơn so với constrained MP @ L3.0/L3.1 (avc1.4d401e/avc1.4d401f), tận dụng khả năng nén của H.264. Tuy nhiên, nó cũng có thể gây giật lag, đứng video hoặc trễ trên các thiết bị yếu và tiêu tốn pin.

Hay HP @ L3.0 (avc1.64001e) và constrained MP @ L3.0 đều là L3.0 nhưng HP sẽ cho kết quả trông đẹp hơn ở những tập tin kích thước nhỏ. Đây là codec mà YouTube từng dùng cho D2G khi chưa có VP9.

H.264/AVC constrained BP video (main and extended video compatible) @ L3 (avc1.42e01e), có thể cân nhắc là lựa chọn tốt cho các thiết bị có hiệu suất thấp, hạn chế tài nguyên. Constrained BP là phiên bản đơn giản hóa của BP, loại bỏ một số tính năng để cải thiện khả năng tương thích.

Bảng sau liệt kê một số ví dụ video codecs cùng profile và cấu hình thông dụng (widely-used profiles).

Table 3-1: Danh sách các video codecs thông dụng

Tương tự là một số ví dụ codec identifiers dành cho audio:

MPEG-4 Audio (MP4 Audio) có base type là “mp4a”.

MPEG-4 AAC (AAC-LC) Profile “mp4a.40.2”

MPEG-4 HE-AAC Profile “mp4a.40.5”

MPEG-4 HE-AAC v2 Profile “mp4a.40.29”

Dolby Digital (AC-3) “ac-3”

Dolby Digital Plus (Enhanced AC-3 hay EC-3) “ec-3”

Tham khảo thêm chi tiết codec parameters tại Codecs in common media types - Web media technologies | MDN (mozilla.org)

Bảng sau chỉ liệt kê danh sách một số các audio codec thông dụng:

Table 3-2: Danh sách các audio codecs thông dụng

Bảng sau mô tả base type của các media codec thông dụng (theo đặc tả của Apple tại Apple HLS specs appendixes)

Table 3-3: Danh sách codec cơ sở (codec base type) thông dụng

Tham khảo

HLS nhận ra 'avc3', 'dvhe', và 'hev1', nhưng Apple không khuyến khích sử dụng.

Apple HLS specs appendixes | Apple Developer Documentation

Mezzanine transcoding

Thực hiện transcode/encode mezzaine theo thông số quy định.

Chi tiết bổ sung trong release sau của đặc tả.

Tham khảo YouTube recommended upload encoding settings - YouTube Help (google.com)

Codec được hỗ trợ (supported output codecs)

Video codecs

Hệ thống PHẢI (MUST) hỗ trợ các codec video H.264/AVC, HEVC/H.265, AV1 hoặc VP9 (chỉ dự phòng) cùng các tính năng (HDR, Dolby Vision) như bảng dưới đây.

Table 3-4: Video codecs (đầu ra) được hỗ trợ

Chú ý VVC/H.266 là tiêu chuẩn nén thế hệ mới được phát triển bởi ITU-T và MPEG, được chuẩn hóa ISO/IEC 23090-3 hay MPEG-I Part 3 vào 2020-06, hiệu quả nén có thể cao hơn đến 50% so với HEVC/H.265, tối ưu cho video 4K/8K, và các ứng dụng gaming, video conferencing VR/AR.

Figure 3-1: Hỗ trợ công nghệ HDR

Đường màu xanh đậm (dark blue) đại diện cho VoD + Live. Đường màu cam đại diện cho Live.

VP9 là phương án dự phòng, được chuẩn bị cho tình huống cụ thể nhằm tăng tính tương thích. Hệ thống ưu tiên codec chính H.265/HEVC và chỉ sử dụng VP9 khi thật sự cần thiết.

Bảng yêu cầu về thông số kỹ thuật (cao nhất) và các tính năng chính của video codec như sau:

Table 3-5: Thông số và tính năng cơ bản của output video codec

Tính tương thích của video codecs

HEVC hiện nay được hỗ trợ rộng rãi trên nhiều nền tảng. Tuy nhiên, HEVC gặp thách thức về vấn đề bản quyền, yêu cầu các nhà sản xuất phải trả phí (khoảng ~$0.3 và các licensing khác liên quan). Do đó, chỉ những thiết bị tầm trung đến cao cấp mới hỗ trợ codec này. HEVC cũng rất kém tương thích với trình duyệt.

Apple HLS specs có các yêu cầu sau với HEVC/H.265

HEVC/H.265 phải sử dụng fMP4 (mục 1.5)

Để tăng tính tương thích HEVC/H.265 NÊN (SHOULD) có profile/level/tier không vượt quá Main 10 Profile, Level 4.0, Main Tier (mục 1.6a)

HEVC PHẢI (MUST) có profile/level/tier không vượt quá Main 10 Profile, Level 5.1, High Tier

Nội dung HDR HEVC phải sử dụng HDR10, HLG, hay Dolby Vision (hiển nhiên không có HDR10+)

AV1 là codec mã nguồn mở và miễn phí bản quyền, đang dần được các dịch vụ phát trực tuyến lớn như YouTube, Netflix, Facebook, và Twitch chấp nhận và sử dụng. Dù vậy AV1 chưa có mặt rộng rãi trên các thiết bị phần cứng so với HEVC/H.265.

Tham khảo mức độ hỗ trợ của các trình duyệt đối với HEVC (caniuse.com) và AV1 (caniuse.com)

Kiểm tra MIME (ISOBMFF) có được trình duyệt hỗ trợ hay không Media MIME Support (cconcolato.github.io)

Trong WWDC24, Apple đã công bố hỗ trợ Dolby Vision Profile 10, là profile AV1 10-bit tương thích với Dolby. Tài liệu What's new in HTTP Live Streaming - 2024 (apple.com) có các điểm quan trọng:

Hỗ trợ AV1 w/ HDR10+ (theo SUPPLEMENTAL-CODECS từ phụ lục Apple HLS specs appendixes)

Hỗ trợ AV1 w/ Dolby Vision 10.x (một số thiết bị) với profiles 10, 10.1 và 10.4. Ví dụ về báo hiệu backward compatibility với CODECS="av01.0.13M.10.0.112",SUPPLEMENTAL-CODECS="dav1.10.09/db4h",VIDEO-RANGE=HLG

Xem thêm chi tiết liên quan HDR (và Dolby Vision) tại [3.6 — Nội dung video HDR (HDR video content)]

Bảng sau tóm tắt tính tương thích giữa các loại thiết và các video codecs

Table 3-6: Devices & video codecs compatibility

Lưu ý: Đối với hầu hết các trình duyệt web, người dùng cuối thường sử dụng phiên bản gần như mới nhất do tính năng tự động cập nhật được bật theo mặc định.

Tham khảo mức độ hỗ trợ của các trình duyệt đối với H.264/AVC (caniuse.com), HEVC (caniuse.com), AV1 (caniuse.com), và vp9 (caniuse.com)

HDR video formats

HDR giúp nâng cao chất lượng hình ảnh bằng cách mở rộng phạm vi độ sáng (dynamic range of brightness) lên hàng nghìn cd/m² (hay nit), và sử dụng không gian màu rộng hơn (Rec. 2020/BT.2020).

So với SDR chỉ giới hạn ở độ sáng 100 nits, dải màu Rec. 709 và 8-bit (16,7 triệu màu), HDR vượt trội hơn hẳn:

Cung cấp độ sáng vượt trội, giúp hiển thị các vùng sáng và tối vượt trội.

Tái hiện màu đen với các sắc độ đen khác nhau, tăng độ tương phản (trên 1000:1), tăng độ chi tiết và tạo chiều sâu cho hình ảnh.

Với độ sâu màu 10-bit/12-bit, dải màu (không gian màu) rộng hơn và khả năng tái tạo màu sắc chính xác.

Dải màu (không gian màu) rộng hơn cũng giúp việc chuyển tiếp màu mượt mà hơn, mang lại hình ảnh tự nhiên và chân thực hơn. HDR giúp giảm hiện tượng phân mảnh màu ví dụ trong các cảnh gradient như bầu trời.

Công nghệ này là yếu tố then chốt (key element) dùng đánh giá chất lượng video 4K UHD, nhất là trên các thiết bị như TV có hỗ trợ.

Table 3-7: Các công nghệ HDR được hỗ trợ

Perceptual quantizer (PQ) transfer function phát triển bởi Dolby.

Hybrid log–gamma (HLG) transfer function phát triển bởi BBC và NHK, tương thích ngược với SDR Ultra HD TV.

Lưu ý một số thương hiệu TV sẽ không hỗ trợ công nghệ HDR nhất định:

Samsung không hỗ trợ Dolby Vision do chọn phát triển HDR10+

Sony's Android TV

Không hỗ trợ HDR10+

Chỉ hỗ trợ Dolby Vision ở một số model tầm trung hay dòng cao cấp, là OLED hoặc LED với local dimming, độ phân giải 4K/8K

Xem thêm chi tiết tại What are the compatible HDR formats on my BRAVIA TV? | Sony AP (sony-asia.com), Compatible HDR formats for your TV | Sony

Audio codecs

Hệ thống PHẢI (MUST) các codec âm thanh đầu ra sau:

Table 3-8: Audio codecs (đầu ra) được hỗ trợ

Nội dung PHẢI (MUST) bao gồm ít nhất một luồng âm thanh AAC (least one stream of AAC) để đảm bảo khả năng tương thích với các thiết bị không hỗ trợ Dolby hoặc các định dạng âm thanh chất lượng cao khác. Ngoài ra, nội dung CÓ THỂ (MAY) bao gồm các luồng âm thanh chất lượng cao như Dolby Digital (AC-3) hoặc các định dạng khác như Dolby Atmos để mang lại trải nghiệm âm thanh nâng cao trên các thiết bị có hỗ trợ các công nghệ này.

Theo mục 2.6, Apple HLS specs, nếu có dụng định dạng Dolby Digital Plus (E-AC-3 hay EC-3) thì PHẢI (MUST) fallback với Dolby Digital (AC-3) cho các thiết bị không hỗ trợ Dolby Digital Plus.

Tính tương thích âm thanh (audio compatibility)

Apple iOS devices không hỗ trợ tốt 5.1 AAC audio codec thay vào đó multi-channel audio phải sử dụng Dolby Digital hay Dolby Digital Plus codecs.

Đối với thiết bị Apple, xem chi tiết tại mục “Audio compatibility” Apple HLS specs appendixes

Hoặc tham khảo tài liệu thông số (đặc tả) kỹ thuật technical specifications của thiết bị cụ thể tại Manuals, Specs, and Downloads - Apple Support

Container formats

Hệ thống PHẢI (MUST) hai loại container format cơ bản dành cho HLS và MPEG-DASH:

MPEG Transport Stream (MPEG-TS)

Fragmented MP4 (fMP4)

Sẵn sàng hỗ trợ CMAF (tương lai gần)

WebM (dự phòng dùng cho web với codec VP9)

Định dạng luồng âm thanh cơ bản (elementary audio stream formats)

Một số luồng cơ sở/cơ bản/trực tiếp dành cho audio (elementary audio stream) có thể được phát trực tiếp mà không cần phải đóng gói (encapsulate) trong một container.

Nếu nội dung chỉ là audio (audio-only content/data), với HLS, hệ thống có thể sử dụng elementary audio stream phân đoạn (segmented audio elementary streams) hoặc fMP4 tùy thuộc vào cách cấu hình của hệ thống.

Để đảm bảo khả năng xử lý các sản phẩm chỉ có âm thanh như podcast và trợ lý ảo (assistant), hệ thống NÊN (SHOULD) hỗ trợ elementary audio stream (nếu được) thay vì đóng gói trong container, bao gồm.

AAC with Audio Data Transport Stream (ADTS) framing

PCM

Xem thêm

Media container formats (file types) - Web media technologies | MDN (mozilla.org)

Với DASH việc hỗ trợ audio-only adaptive streaming playback nói chung là không được tốt và không được tối ưu. Do đó, trong trường hợp cần một hệ thống riêng cho việc streaming audio, nên cân nhắc sử dụng các công nghệ khác như Icecast.

Tham khảo ví dụ trực tiếp tại Audio only stream example (dashif.org).

Tương thích codecs và containers

Việc lựa chọn codecs nào có thể hỗ trợ phụ thuộc phần lớn vào chính thiết bị, hệ điều hành hay trình duyệt (device/OS/browser, nói chung là phía client) mà người dùng sử dụng. Hiện tại, lựa chọn phổ biến và tương thích nhất để phân phối nội dung video trên nhiều thiết bị (cross-device platform) vẫn đang là H.264/AVC và AAC.

Table 3-9: Tương thích containers và codecs

Tính năng âm thanh Dolby (Dolby audio features)

Hệ thống hỗ trợ tính năng âm thanh Dolby chi tiết như sau.

Hỗ trợ Dolby Atmos (Dolby Atmos support)

Chi tiết bổ sung trong release sau của đặc tả.

Xem thêm thông tin chi tiết sử dụng Dolby AC-4 với HLS và DASH

Dolby AC-4 and HTTP Live Streaming

Dolby AC-4 in MPEG-DASH for Online Delivery

Xem thêm

What is Dolby Digital Plus JOC? (dolby.com)

Hỗ trợ Dolby Digital Plus

Đối với DASH, cụ thể là MPD manifest:

Thuộc tính codecs (codecs attribute) là bắt buộc và phải là “ec-3” cho Dolby Digital Plus (DD+)

Đối với DD+ bitstream mang nội dung Dolby Atmos (carry Dolby Atmos content), PHẢI (MUST) thêm mô tả SupplementalProperty.

Xem thêm thông tin tại

Dolby Digital Plus Online Delivery Content Creation — System Development Guide

Phần quy định dành cho DASH Media Presentation Description with Dolby Digital Plus › Adaptation sets

Nội dung video HDR (HDR video content)

Một số các ràng buộc về nội dung video HDR dành cho thiết bị Apple được quy định trong Apple HLS specs

Theo mục 1.7, HDR video dùng HEVC/H.265 PHẢI (MUST) là HDR10, HLG hoặc Dolby Vision.

Theo mục 9.24, nếu cung cấp nội dung HDR thì NÊN (SHOULD) có cả Dolby Vision và HDR10.

Một số công nghệ HDR codec có khả năng tương thích ngược với các HDR codec khác.

Nghĩa là metadata sẽ bị bỏ qua khi được giải mã bởi codec tương thích.

Ví dụ, Dolby Vision 8.4 và 10.4 tương thích với HLG hoặc Dolby Vision 8.1 và 10.1 tương thích với HDR10

SUPPLEMENTAL-CODECS cho phép mô tả các codec nâng cao có khả năng tương thích ngược với codec cơ bản (như Dolby Vision tương thích với HLG hoặc HDR10).

Dưới đây là ví dụ về giá trị SUPPLEMENTAL-CODECS (từ phụ lục Apple HLS specs appendixes)

Table 3-10: SUPPLEMENTAL-CODECS và backward-compatibility

Hỗ trợ Dolby Vision (Dolby Vision support)

Với HLS, loại video sẽ được truyền tải là sử dụng thẻ EXT-X-STREAM-INF hoặc EXT-X-I-FRAME-STREAM-INF và thuộc tính CODECS liên quan (CODECS attribute). Thuộc tính CODECS của EXT-X-STREAM-INF (hoặc EXT-X-I-FRAME-STREAM-INF) bao gồm một giá trị gồm ba phần, ngăn cách bởi dấu chấm, để báo hiệu thông tin về codec, profile và level của luồng Dolby Vision được tham chiếu. Đối với một luồng Dolby Vision, giá trị của video codec được tạo thành theo định dạng sau:

[Dolby Vision fourCC].[Profile string].[Level ID]

Trong đó

Dolby Vision fourCC

Profile string

Level ID

Giao thức streaming và DRM (streaming protocols & DRM)

Hệ thống PHẢI (MUST) hỗ trợ các streaming protocols sau:

HLS

DASH

và progressive download/pseudo-streaming (thông thường chỉ sử dụng cho tính năng D2G hay trong managed network)

Bảo vệ nội dung là yêu cầu rất quan trọng của hệ thống streaming. Nó ảnh hưởng đến việc chọn giao thức streaming, containers, và codecs. Ba công nghệ DRM chính là Google Widevine, Apple FairPlay và Microsoft PlayReady. Mỗi công nghệ có sự tương thích với các nền tảng và giao thức khác nhau. Các công nghệ DRM có sự ưu tiên riêng cho hệ sinh thái liên quan và bị ảnh hưởng bởi các yếu tố cạnh tranh cũng như độc quyền.

FairPlay Streaming (FPS) là công nghệ DRM của Apple được thiết kế để bảo vệ nội dung trên các thiết bị của chính Apple (cụ thể Apple mobile devices, Apple TV và Safari trên OS X). Các thiếu bị này sử dụng giao thức streaming “độc quyền” của Apple là HLS. Do đó, HLS gần như mặc định sẽ sử dụng FairPlay.

Cả ba công nghệ DRM đều sử dụng AES-128. Tuy nhiên, Widevine và PlayReady ban đầu sử CTR mode (counter – block cipher mode of operation) thì FairPlay lại sử dụng CBC mode (cipher block chaining). Vì vậy, có thể lựa chọn giữa Widevine và PlayReady, nhưng không thể lựa chọn Widevine và PlayReady để thay thế FairPlay. Chỉ gần đây, Widevine và PlayReady mới có chế độ CBC, cho phép hoạt động với HLS.

Chiều ngược lại, FairPlay là công nghệ DRM độc quyền dành riêng cho hệ sinh thái của Apple. Nghĩa là nếu muốn phân phối nội dung trên nền tảng khác như Android hoặc Windows, thì cần sử dụng công nghệ DRM khác.

Thách thức khi lựa chọn DRM là tính tương thích sẽ ảnh hưởng tiềm tàng đến hiệu suất và rủi ro xảy ra lỗi. Dù HLS hoạt động tốt với FairPlay trong hệ sinh thái Apple, nhưng điều này không đảm bảo rằng nó sẽ hoạt động hiệu quả trên các nền tảng khác với DRM khác.

Bảng sau minh họa tính tương thích (compatibility matrix) giữa giao thức streaming và DRM.

Table 3-11: Tương thích streaming protocols và DRM

Như đã nói có sự tương thích nhất định giữa DRM và thiết bị. Ví dụ cụ thể FairPlay chỉ hoạt động trên các thiết bị Apple. Thiết bị có thể chia ra thành các nhóm theo 3 tiêu chí chính loại thiết bị (device type), hệ điều hành (OS) và trình duyệt (web brower) như sau:

Smart TV (CTV nói chung), chia làm các loại chính theo OS

Android TV

Samsung Tizen

LG webOS

Smart TV khác với sử dụng web technologies (web-based apps)

Thiết bị di động (mobile devices) bao gồm tức smartphone và tablet

Android

iOS

Và web browsers

Browser trên desktop/laptop

Bao gồm cả desktop/laptop apps dùng web technologies như Electron

Browser trên trên mobile

Bao gồm mobile apps dùng web technologies (hay dùng WebView) như Ionic

Bảng sau minh họa tính tương thích giữa DRM và loại thiết bị, hệ điều hành, trình duyệt.

Table 3-12: Tương thích giao thức streaming và thiết bị/OS/browser

Phần sau chỉ tóm tắt các giao thức streaming (streaming protocols) tức HLS và DASH, giải thích ngắn gọn về các thẻ hỗ trợ (supported tags) để cung cấp cái nhìn tổng quan về cách sử dụng và các tính năng.

Tham khảo tài liệu kỹ thuật của HLS tại RFC 8216 (bản mới nhất draft-pantos-hls-rfc8216bis-15 (ietf.org)) giới hiệu HTTP Live Streaming (HLS) và best practice Apple HLS specs tại Apple Developer.

Xem thêm đặc tả DASH trong ISO/IEC 23009 và các tài liệu tại diễn đàn DASH Industry Forum | Catalyzing the adoption of MPEG-DASH (dashif.org)

Giao thức cast (cast protocols)

Tính năng thumbnail preview (feature)

Hệ thống hỗ trợ tính năng thumbnail preview (chỉ VOD) thông qua side-loaded WebVTT (API trả về) với JPEG/PNG images/sprites (spritesheet).

Các thực hiện này không phụ thuộc vào giao thức stream HLS hoặc DASH và chỉ cần player hỗ trợ.

KHÔNG ĐƯỢC (MUST NOT) sử dụng tham chiếu ảnh rời mà không có dữ liệu xywh (without xywh data).

Xem thêm yêu cầu chi tiết về “trick play” trong mục 6, Apple HLS specs

Thông số kỹ thuật của spritesheets chủ yếu gồm các phần:

Tần số ảnh thumbnail (image interval hay frame interval), tức bao nhiêu giây sẽ lấy một ảnh

Thông số kỹ thuật về ảnh thumbnail (tức một item của spritesheet)

Về kích thước spritesheet, cụ thể là tile size

Việc cung cấp quá nhiều thumbnails là không cần thiết vì progress timeline bar (hay seek bar) sẽ có kích thước nhất định (giới hạn về kích thước bằng chiều ngang của thiết bị).

Quá nhiều thumbnails thậm chí gây khó khăn trong việc điều hướng.

Cue points cần một kích thước nhất định để nhận hover.

Ngoài ra kích thước dung lượng spritesheets sẽ lớn hoặc phải chia thành nhiều spritesheets.

Do đó cần điều chỉnh tần số lấy thumbnails khác nhau tùy độ dài nội dung.

Hệ thống PHẢI (MUST) thực hiện lấy thumbnails và tạo spritesheet theo từng khoảng thời lượng của video:

Table 3-13: Thiết lập tần số thời gian khi tạo thumbnails sprites

Kích thước spritesheet tức tile = rows × cols nên được tối ưu hóa để:

Kích thước spritesheet có ratio hợp lý dễ quản lý, tốt nhất là vẫn gần tỷ lệ 16:9

Số ảnh / spritesheet không quá nhiều hoặc quá ít

Số lượng dư thừa ảnh phải hợp lý (số slot thuộc spritesheet cuối cùng chưa lấp đầy)

Ví dụ thông số của ảnh spritesheet của một movie có thời lượng 45 phút có thể thiết lập như sau:

Tỷ lệ ảnh thumbnail: 16 × 19

Kích thước ảnh thumbnail: 320 × 180

Frame interval: 10 seconds

Số lượng ảnh cần: 45 m = 2700 s › 2700 / 10 = 270 ảnh

Định dạng ảnh: JPEG

Chất lượng ảnh (compression): khoảng 85%

Kích thước tile: 12 × 12 tiles tức 144 ảnh / spritesheet

Giữ đúng tỷ lệ 16:9 cho ảnh spritesheet

Chỉ cần 2 spritesheet cho 270 ảnh cho video 45 phút

2 spritesheet × 144 ảnh = 288 ảnh › sẽ dư 18 ảnh

Vì video gốc có thể có tỷ lệ khung hình dạng cinematic widescreen và không phải 16:9, nên khi tạo ảnh thumbnail với tỷ lệ 16:9, cần phải crop (fit) để giữ đúng tỷ lệ mà không bị méo hình và tránh xuất hiện viền đen.

Ví dụ command tạo spritesheet với FFmpeg

ffmpeg -i input.mp4 -vf "fps=1/10, crop='min(iw,ih*16/9)':'min(ih,iw*9/16)', scale=320:180, tile=12x12" -q:v 4 -frames:v 1 spritesheet_%02d.jpg

Giải thích các tham số:

-i input.mp4:

Tham số chỉ định video đầu vào.

-vf "...":

-vf là tùy chọn để áp dụng các video filter.

Các filter này được định nghĩa trong dấu ngoặc kép sau -vf.

fps=1/10:

Lấy 1 frame mỗi 10 giây, fps=1/10 sẽ lấy một ảnh thumbnail mỗi 10 giây.

crop='min(iw,ih*16/9)':'min(ih,iw*9/16)':

Thao tác crop (cắt) video để đảm bảo tỷ lệ khung hình là 16:9 mà không bị méo hình.

iw và ih là chiều rộng (width) và chiều cao (height) của video gốc.

Công thức này sẽ cắt video sao cho chiều rộng và chiều cao được điều chỉnh để phù hợp với tỷ lệ 16:9 mà không bị viền đen hay méo hình.

min(iw, ih*16/9) cắt theo chiều rộng sao cho tỷ lệ 16:9 được giữ.

min(ih, iw*9/16) cắt theo chiều cao sao cho tỷ lệ 16:9 được giữ.

scale=320:180:

Thay đổi kích thước của ảnh thumbnail thành 320 × 180 px tiêu chuẩn.

tile=12×12:

Sắp xếp các ảnh thành spritesheet với kích thước 12x12 tiles, chứa 12 hàng và 12 cột, tức là 144 ảnh mỗi spritesheet.

Nếu bạn có ít hơn 144 ảnh, phần còn lại của spritesheet sẽ bị trống (hoặc chứa ảnh dư).

-q:v 4:

Xác định chất lượng nén của ảnh JPEG.

-q:v 4 có nghĩa là chất lượng ảnh sẽ khoảng trên 85% cân bằng giữa độ nén và kích thước (phạm vi từ 1 đến 31, với 1 là chất lượng cao nhất và 31 là chất lượng thấp nhất).

-frames:v 1:

Chỉ định số lượng frames mà FFmpeg sẽ xuất ra, -frames:v 1 có nghĩa là chỉ xuất ra một spritesheet duy nhất, thay vì xuất từng ảnh riêng lẻ.

spritesheet_%02d.jpg:

Đây là mẫu (template) tên file cho ảnh đầu ra, %02d là một placeholder cho số thứ tự của mỗi file ảnh với padding 0.

Ví dụ, nếu có nhiều spritesheet (nếu cần), tên file sẽ là spritesheet_01.jpg, spritesheet_02.jpg, ....

Script Python dùng để tạo file VTT có thể như sau:

import os

# Video and thumbnail settings

cols = 12  # Number of columns in the spritesheet

rows = 12  # Number of rows in the spritesheet

image_width = 320  # Width of each thumbnail image

image_height = 180  # Height of each thumbnail image

time_interval = 10  # Time interval for each thumbnail (10 seconds)

# Video duration (in seconds)

video_duration = 2700  # Example: 45 minutes = 2700 seconds

# Create VTT file

output_vtt = 'thumbnails.vtt'

# Total number of thumbnails to generate

num_images = video_duration // time_interval  # Total number of thumbnails (every 10 seconds)

# Create and open the VTT file

with open(output_vtt, 'w') as f:

f.write('WEBVTT\n\n')  # VTT header

# Track the current spritesheet index

spritesheet_index = 1

for img_counter in range(num_images):

# Calculate start and end times for each thumbnail

start_time = img_counter * time_interval

end_time = (img_counter + 1) * time_interval

# Format the times to VTT format (h:mm:ss.mmm)

start_time_str = f'{start_time // 60:02}:{start_time % 60:02}.000'

end_time_str = f'{end_time // 60:02}:{end_time % 60:02}.000'

# Calculate the position of the image in the spritesheet

col = img_counter % cols  # Current column in the spritesheet

row = img_counter // cols  # Current row in the spritesheet

# If we exceed the current spritesheet size, move to the next spritesheet

if img_counter >= (spritesheet_index * cols * rows):

spritesheet_index += 1

col = 0  # Reset column

row = 0  # Reset row

# Calculate the xywh (coordinates) for the image

x = col * image_width

y = row * image_height

w = image_width

h = image_height

# Create the spritesheet filename (e.g., spritesheet_01.jpg)

spritesheet_name = f"spritesheet_{spritesheet_index:02d}.jpg"

# Format the VTT entry for each thumbnail

vtt_entry = f'Img {img_counter + 1}\n{start_time_str} --> {end_time_str}\n{spritesheet_name}#xywh={x},{y},{w},{h}\n\n'

# Add comment block with row and column information as NOTE

row_col_comment = f'NOTE\nRow: {row}, Col: {col}\n'

# If the spritesheet changes, add a transition comment

if col == 0 and row == 0 and img_counter > 0:  # Transition to a new spritesheet

f.write(f'NOTE\nTransitioning to {spritesheet_name}\n')

# Write the comment and the VTT entry to the file

f.write(row_col_comment)

f.write(vtt_entry)

print(f'VTT file has been created: {output_vtt}')

File VTT sẽ dạng như sau:

WEBVTT

NOTE

Row: 0, Col: 0

Img 1

00:00.000 --> 00:10.000

spritesheet_01.jpg#xywh=0,0,320,180

NOTE

Row: 0, Col: 1

Img 2

00:10.000 --> 00:20.000

spritesheet_01.jpg#xywh=320,0,320,180

NOTE

Row: 1, Col: 0

Transitioning to spritesheet_02.jpg

...

NOTE

Row: 11, Col: 11

Img 144

23:50.000 --> 24:00.000

spritesheet_01.jpg#xywh=3520,1980,320,180

NOTE

Transitioning to spritesheet_02.jpg

NOTE

Row: 0, Col: 0

Img 145

24:00.000 --> 24:10.000

spritesheet_02.jpg#xywh=0,0,320,180

Tính năng chapter markers & cue points

Hệ thống hỗ trợ tính năng chapter markers & cue points (chỉ VOD) thông qua side-loaded WebVTT (API trả về).

Chi tiết bổ sung trong release sau của đặc tả.

ÂM THANH VÀ PHỤ ĐỀ

Thẻ ngôn ngữ (language tags)

Thẻ ngôn ngữ (language tag) tuân thủ best practice quy định tại RFC 5646 (tức BCP 47). Language tag có cấu trúc bao gồm nhiều subtag dạng language-extlang-script-region-variant-extension-privateuse 
với ý nghĩa như sau:

Language (bắt buộc) chỉ định ngôn ngữ chính (primary language subtag), có thể dùng ISO 639-1 alpha-2 (tức 2 ký tự để chỉ định ngôn ngữ, two-letter language codes) hoặc ISO 639-3 alpha-3 (3 ký tự).

Extlang (tùy chọn) mã ngôn ngữ mở rộng, thường là một mã 3 ký tự tuy nhiên ít được sử dụng. Ví dụ thường gặp như tiếng Quảng Đông là zh-yue (Cantonese Chinese)

Script (tùy chọn) gồm 4 ký tự, xác định hệ thống chữ viết được sử dụng (theo tiêu chuẩn ISO 15924, names of scripts). Ví dụ thường gặp zh-Hant (tiếng Hoa viết bằng chữ Hán phồn thể), zh-Hans (tiếng Hoa viết bằng chữ Hán giản thể)

Region (tùy chọn) mã vùng gồm 2 ký tự (ISO 3166-1 alpha-2) hoặc 3 ký tự (ISO 3166-1 alpha-3) để chỉ ra khu vực địa lý hoặc quốc gia. Ví dụ fr-FR cho tiếng Pháp tại Pháp và fr-CA cho tiếng Pháp tại Canada (như Quebec).

Variant (tùy chọn) chỉ biến thể của ngôn ngữ, ít khi sử dụng. Ví dụ cụ thể như phiên âm Latinh tiếng Trung dùng Pinyin (bính âm Hán ngữ) chỉ định bằng zh-Latn-pinyin. Nó giúp phân biệt với các phiên âm Latinh tiếng Trung khác ví dụ như Wade-Giles zh-Latn-wadegile.

Extension (tùy chọn) là mã mở rộng để thêm các loại thông tin bổ sung cho ngôn ngữ. Tùy chọn mở rộng có thể bắt đầu bằng tiền tố “-t” (theo RFC 6497, “BCP 47 Extension T - Transformed Content”), hay tiền tố “-u” (theo RFC 6067, “BCP 47 Extension U”).

Private use (tùy chọn) là mã sử dụng cho mục đích riêng, bắt đầu bằng tiền tố “-x-”.

Hệ thống PHẢI (MUST) thực hiện chỉ định language tag theo đặc tả như sau:

Sử dụng ISO 639-1 alpha-2 (tức two-letter language codes) để chỉ định primary language subtag.

Sử dụng extlang subtag dạng language-extlang theo ISO 639-3 nếu có nhiều track âm thanh cùng ngôn ngữ chính. Ví dụ hay gặp là zh-yue cho tiếng Quảng Đông và zh tiếng Trung Quốc phổ thông/tiếng Quan Thoại (Mandarin Chinese, zh-cmn ít dùng).

Sử dụng script subtag dạng language-script (hay writing systems) theo ISO 15924 nếu có nhiều subtitles cùng ngôn ngữ chính. Ví dụ hay gặp là zh-Hant (tiếng Hoa viết bằng chữ Hán phồn thể/Traditional Han), zh-Hans (tiếng Hoa viết bằng chữ Hán giản thể/Simplified Han).

Sử dụng region (tùy chọn) dạng 2 ký tự (ISO 3166-1 alpha-2)

Sử dụng private use subtag dạng language-privateuse cần chỉ định theo thông tin về ngôn ngữ ví dụ cụ thể là để phân biệt 2 track âm thanh vi-x-dubbed dành cho lồng tiếng và vi-x-vo dành cho thuyết minh.

Tóm lại hệ thống PHẢI (MUST) sử dụng RFC 5646 (tức BCP 47) với quy định như sau:

2 ký tự cho language subtag theo ISO 639-1 alpha-2

3 ký tự cho extlang subtag theo ISO 639-3

4 ký tự cho script subtag theo ISO 15924

Và 2 ký tự region subtag theo ISO 3166-1 alpha-2

Sự khác biệt về số ký tự và thứ tự cộng thêm thứ tự các thành phần này giúp dễ dàng xác định mục đích dùng cho ngôn ngữ hay chữ viết. Cách tổ chức này cũng đáp ứng đầy đủ các nhu cầu sử dụng

Tham khảo các tiêu chuẩn liên quan:

ISO 639-1 Language code list (loc.gov), ISO 639 Code Tables (sil.org)

IANA registry (ISO 15924) Language subtag registry (iana.orh)

ISO 3166-1 Country codes (iso.org)

Bảng sau liệt kê một số ví dụ thông dụng (sẽ sử dụng trong hệ thống):

Table 4-1: Ví dụ về cách xác định ngôn ngữ và chữ viết

Tên track (track names)

Tên track sẽ ưu tiên do đội Nội dung và vận hành thiết lập thủ công (manual) thông qua tools vận hành và theo nhu cầu thực tế. Nếu không có thiết lập thủ công, hệ thống sẽ áp dụng (hỗ trợ áp dụng) theo quy tắc định sẵn.

Tên audio track và phụ đề theo quy tắc thường sẽ bao gồm các thông tin (nếu có):

Thông tin về ngôn ngữ (language)

Thông tin về vai trò của track (role hay vai trò alternative)

Chất lượng với âm thanh (với audio track)

Tên track được trình bày theo quy tắc cơ bản sau:

Đầu tiên hiển thị thông tin về ngôn ngữ

Ví dụ “Tiếng Trung”, “Tiếng Hàn” (xác định theo language tags).

Nếu không có thông tin về ngôn ngữ (und – undetermined), hệ thống sẽ sử dụng “Âm thanh 1”, “Âm thanh 2” …

Tiếp theo là vai trò của track nằm trong dấu ngoặc vuông (enclosed in square brackets), ví dụ “Tiếng Hàn [Gốc]” (tiếng anh là “Korean [Original]”).

Có thể rút gọn với tiếng Việt do là ngôn ngữ được ưu tiên theo mặc định theo trường hợp cụ thể ví dụ “Thuyết minh” › “Tiếng Hàn [Gốc]” thay cho “Tiếng Việt [Thuyết minh]” › “Tiếng Hàn [Gốc]”.

Xem thêm chi tiết phần [4.2.1 — Track âm thanh gốc] (về vai trò track âm thanh gốc).

Thông tin bổ sung như chất lượng sẽ nằm trong dấu ngoặc đơn (enclosed in parentheses), ví dụ “Tiếng Hàn [Gốc] (Dolby Atmos)” › “Tiếng Hàn (Dolby Digital 5.1)”.

Track âm thanh gốc

Âm thanh gốc là khái niệm chỉ phiên bản âm thanh ban đầu, không qua chỉnh sửa hoặc dịch thuật sang ngôn ngữ khác.

Âm thanh gốc thường có chất lượng cao nhất, là multi-channel, surround hay immersive audio ở định dạng cao cấp như Dolby Digital Plus, Dolby Atmos.

Không phải tất cả các thiết bị hay platform đều hỗ trợ âm thanh chất lượng cao:

Âm thanh gốc sẽ phải có các bản sao dự phòng (fallback) sử dụng các codec đơn giản hơn để đảm bảo khả năng tương thích.

Khi có track âm thanh gốc, gần như sẽ có nhiều track âm thanh fallback.

Bản sao dự phòng (fallback) chất lượng thấp hơn sẽ không còn mang ý nghĩa âm thanh gốc.

Âm thanh gốc sẽ bao hàm cả ý nghĩa là ngôn ngữ gốc (của nội dung).

Khái niệm “tiếng gốc” hay “ngôn ngữ gốc” có thể hiểu là ngôn ngữ của track âm thanh gốc.

Dù phản ánh ngôn ngữ nhưng lại không rõ là ngôn ngữ gì

Không cung cấp thêm thông tin gì hữu ích cho người dùng ví dụ như chất lượng hay tính chất hay vai trò của track âm thanh.

Ví dụ như sau:

Nếu dùng “Tiếng gốc (Dolby Atmos)” › “Tiếng Việt” (track AAC fallback)

Liệu user có hiểu “tiếng gốc” cũng là tiếng Việt?

Không thể hiện rõ được vai trò của track dự phòng (quan hệ fallback và original).

Nếu dùng “Tiếng gốc (Dolby Atmos)” › “Tiếng gốc (Dolby Digital 5.1)” › “Tiếng gốc“

Tức trường hợp hay gặp là có nhiều bản sao dự phòng (fallback)

Rất “kỳ lạ” về hiển thị, gây khó hiểu khi lặp lại những vẫn không biết ngôn ngữ là gì.

Tóm lại cụm từ “tiếng gốc” không mang nhiều ý nghĩa, và không cần thiết.

Lưu ý:

Với track âm thanh, không dùng khái niệm “tiếng gốc” hay “ngôn ngữ gốc”.

Ưu tiên sử dụng khái niệm “âm thanh gốc” thay cho “tiếng gốc” hay “ngôn ngữ gốc” nếu được.

Không phải tình huống nào cũng có âm thanh gốc.

Ví dụ một phim dù chỉ có một track âm thanh duy nhất, nhưng track âm thanh này đã qua chỉnh sửa (ví dụ là fallback) thì nó cũng vẫn không phải là âm thanh gốc.

Nếu xác định được ngôn ngữ, sẽ hiển thị ví dụ “Tiếng Trung”, “Tiếng Hàn”

Nếu không xác định được ngôn ngữ, sử dụng “Âm thanh 1”.

Khái niệm âm thanh gốc chỉ nên dùng khi đi kèm với track âm thanh có vai trò thay thế (alternative).

Nếu không có vai trò thay thế, không cần thể hiện thông tin âm thanh gốc.

Nếu có thể phân biệt thông qua chất lượng, không cần thể hiện thông tin âm thanh gốc (nếu không có nhu cầu hoặc không đủ thông tin). Có thể ngầm định track chất lượng cao là gần nhất với âm thanh gốc.

Ví dụ một phim chỉ có một track âm thanh âm thanh chất lượng cao, và các bản sao dự phòng (fallback).

Do không có vai trò thay thế, nên không cần thông tin âm thanh gốc.

Nếu có thông tin ngôn ngữ, hiển thị “Tiếng Trung (Dolby Atmos)” › “Tiếng Trung (Dolby Digital 5.1)” › “Tiếng Trung“.

Không có thông tin ngôn ngữ, hiển thị “Âm thanh 1 (Dolby Atmos)” › “Âm thanh 2 (Dolby Digital 5.1)” › “Âm thanh 3“.

Track âm thanh gốc được đội Nội dung và Vận hành xác định thủ công (manual) thông qua tools vận hành. Khi không có thông tin chỉ định track âm thanh gốc, việc xác định xem một track có phải là âm thanh gốc hay không rất khó khăn. Hơn nữa, không nhất thiết phải tự xác định track âm thanh gốc

Không phải lúc nào cũng có âm thanh gốc, nhất là nội dung VOD thường đã qua transcode.

Ví dụ trong tên track “Tiếng Hàn [Gốc] (Dolby Atmos)”, phần thông tin vai trò “[Gốc]” có thể mang các ý nghĩa sau:

Có thể là âm thanh gốc thật sự

Hoặc chỉ là bản sao của âm thanh gốc

Nếu đã phân biệt được qua ngôn ngữ và chất lượng, không cần tự xác định âm thanh gốc khi thiếu thông tin.

Thay vì hiển thị “Tiếng Hàn [Gốc] (Dolby Atmos)” › “Tiếng Hàn (Dolby Digital 5.1)” › “Tiếng Hàn”, chỉ cần hiển thị “Tiếng Hàn (Dolby Atmos)” › “Tiếng Hàn (Dolby Digital 5.1)” › “Tiếng Hàn” mà vẫn không mất quá nhiều thông tin.

Ngay cả trường hợp chỉ có duy nhất một track âm thanh › chưa chắc đây là âm thanh gốc

Có thể không hiển thị danh sách (lựa chọn) audio track

Nếu có hiển thị danh sách (lựa chọn)

Hiển thị tên ngôn ngữ nếu xác định được như “Tiếng Trung”, “Tiếng Hàn”

Nếu không xác định được ngôn ngữ, hiển thị “Âm thanh 1”

Chỉ có một trường hợp CÓ THỂ được xem là đủ thông tin để tự xác định âm thanh gốc

Nếu chỉ có một track âm thanh chất lượng cao và các track fallback.

Track lồng tiếng (dubbed) và thuyết minh (voice-over) nếu có, chắc chắn không phải là âm thanh gốc.

Track âm thanh chất lượng cao nhất CÓ THỂ xem là (gần nhất với) track âm thanh gốc.

Nếu xác định được ngôn ngữ thể hiện dạng “Tiếng Hàn [Gốc] (Dolby Atmos)” › “Tiếng Hàn (Dolby Digital 5.1)” › “Tiếng Hàn”.

Nếu không xác định được ngôn ngữ, hiển thị “Âm thanh 1 (Dolby Atmos)” › “Âm thanh 2 (Dolby Digital 5.1)” › “Âm thanh 3”.

Tóm lại:

Không phải lúc nào cũng có âm thanh gốc, nhất là track âm thanh gốc thật sự

Track âm thanh gốc được đội Nội dung và Vận hành xác định thủ công.

Quy tắc đặt tên

Quy tắc này là guideline chung, áp dụng cho cả việc chỉ định thủ công (qua tools vận hành) và tự động xác định bởi packager, player.

Ưu tiên xác định ngay từ khâu chuẩn bị (đầu vào cho packager) › đến packaging › ra manifest › lên nội dung › player (cung cấp qua API).

Chỉ khi không có thông tin xác định trước, packager hay player mới tự động sử dụng các thông tin sẵn có của track để tạo tên hợp lý.

Đối với packager, điều này có nghĩa là không có thông tin đầu vào.

Đối với player, điều này có nghĩa là không nhận được thông tin từ back-end API và không có tên trong manifest.

Mục tiêu là đảm bảo dễ hiểu, cung cấp đủ thông tin và giúp người dùng phân biệt được các track với nhau.

Các thông tin này PHẢI (MUST) được trình bày theo cách sau:

Tên ngôn ngữ ví dụ “Tiếng Trung”, “Tiếng Hàn”

Nếu ngôn ngữ xác định, PHẢI (MUST) hiển thị tên ngôn ngữ (ngoại trừ tiếng Việt có thể rút gọn chỉ thể hiện vai trò như “Lồng tiếng” và “Thuyết minh”).

Sử dụng “Âm thanh 1”, “Âm thanh 2” khi không xác định được tên ngôn ngữ hoặc không kiểm soát được thông tin ngôn ngữ như trường hợp tiếp sóng hoặc sự kiện sử dụng nhiều ngôn ngữ mà không cần xác định.

Nếu ngôn ngữ cần có thông tin bổ sung, thông tin bổ sung sẽ nằm trong dấu ngoặc đơn (enclosed in parentheses). Ví dụ “Tiếng Bồ Đào Nha (Brazil)” hay “Tiếng Tây Ban Nha (Mỹ Latinh)”.

Với phụ đề thực hiện hiển thị thông tin bổ sung về chữ viết theo cách tương tự “Tiếng Trung (Giản thể)” và “Tiếng Trung (Phồn thể)”.

Nếu ngôn ngữ là tiếng Việt (và ngôn ngữ hiển thị của ứng dụng là tiếng Việt), tên ngôn ngữ có thể được rút gọn. Ví dụ “Lồng tiếng” và “Thuyết minh” thay cho “Tiếng Việt [Lồng tiếng]” và “Tiếng Việt [Thuyết minh]”.

Sau tên ngôn ngữ, hiển thị vai trò (role) hay thông tin thể hiện âm thanh thay thế (alternative) trong dấu ngoặc vuông (enclosed in square brackets), ví dụ: “Tiếng Hàn [Gốc]” (tức “Korean [Original]” trong tiếng Anh).

Thông tin ngôn ngữ tiếng Việt CÓ THỂ (MAY) được rút gọn, chỉ giữ lại vai trò ví dụ dùng “Thuyết minh” › “Tiếng Hàn [Gốc]” thay cho “Tiếng Việt [Thuyết minh]” › “Tiếng Hàn [Gốc]”

Lưu ý nếu không đủ thông tin thì không nhất thiết phải xác định âm thanh gốc.

Nếu ngôn ngữ ứng dụng không phải tiếng Việt, ví dụ là tiếng Anh, vẫn hiển thị đầy đủ, không rút gọn “Vietnamese [Dubbed]” › “Vietnamese [Voice-over]”.

Thông tin về codec, cấu hình và chất lượng âm thanh.

Hiển thị thông tin về codec và chất lượng âm thanh trong dấu ngoặc đơn (enclosed in parentheses), ví dụ: “Tiếng Hàn (Dolby Digital Plus 7.1)”.

Chỉ hiển thị cấu hình kênh cho âm thanh vòm surround sound như 5.1/7.1, bỏ qua thông tin mono và stereo (2.0/2.1).

Track âm thanh gốc thông thường là track chất lượng cao. Các track bản sao của âm thanh gốc sẽ có vai trò dự phòng (fallback).

Chỉ hiển thị chất lượng cao (lossless, high-quality) như Dolby Atmos, Dolby Digital Plus, Dolby Digital, không hiển thị thông tin codec thông dụng hoặc fallback.

Codec lossless như FLAC/ALAC có thể ghi rõ, ví dụ “Tiếng Hàn [Gốc] (FLAC)”, “Tiếng Hàn [Gốc] (ALAC)”.

Có thể dùng dạng chung ví dụ “Tiếng Hàn [Gốc] (Lossless)” cho codec lossless không phổ biến, kể cả uncompressed như WAV, PCM.

Nếu hai audio track giống nhau cả codec và cấu hình channel, xem xét [Bitrate] › sau đó tới [Sampling rate].

Cùng stereo AAC, khác nhau bitrate, hiển thị “Tiếng Hàn (320 kbps)” › “Tiếng Hàn (128 kpbs)”.

Cùng stereo FLAC, bitrate nhưng khác sampling rate hiển thị “Tiếng Hàn (FLAC 96 kHz)” › “Tiếng Hàn (FLAC 48 kHz)” (hiếm khi xảy ra trong thực tế).

Nếu cả hai thông tin [Bitrate] lẫn [Sampling rate] vẫn không thể phân biệt, cần thực hiện thêm suffix “ 1”, “ 2” cho phần tên trước đó.

Ví dụ có cả 2 track AAC đều là Tiếng Hàn, 128 kpbs, 48 kHz, không có thông tin vai trò hay không rõ vai trò thực hiện thêm suffix sau tên ngôn ngữ “Tiếng Hàn 1” và “Tiếng Hàn 2”.

Hiển thị thông tin với Dolby Atmos

Chỉ hiển thị “Dolby Atmos” mà không cần ghi rõ codec sử dụng (underlying codec).

Không hiển thị cấu hình channel với Dolby Atmos ví dụ “Thuyết minh” › “Tiếng Hàn [Gốc] (Dolby Atmos)” › “Tiếng Hàn” (fallback).

Dolby Atmos không yêu cầu phải có đầy đủ loa vật lý (speaker). Ngay cả khi không đủ loa, người xem vẫn có thể trải nghiệm một phần của hiệu ứng âm thanh Dolby Atmos.

Hầu hết TV và soundbar sử dụng công nghệ giả lập của Dolby Atmos (hiểu đơn giản là software solution) để mô phỏng trải nghiệm âm thanh 3D/ immersive mà không cần có đủ 5.1.4 loa hoặc loa trần (overhead speaker, loa trên cao).

Dolby Atmos có thể dùng nhiều cấu hình như loa ảo (virtual speaker setup), cấu hình tận dụng loa trần (overhead speaker) có sẵn, dùng loa hỗ trợ Dolby Atmos (Dolby Atmos-enabled) mà không cần lắt đặt loa trên cao.

Một số ví dụ hay gặp:

Phim tiếng Việt, track âm thanh gốc Dolby Atmos (đã xác định bởi đội Nội dung và Vận hành), các bản sao dự phòng (fallback) là Dolby Digital Plus 5.1, và AAC.

Ưu tiên hiển thị “Tiếng Việt [Gốc] (Dolby Atmos)” › “Tiếng Việt (Dolby Digital 5.1)” › “Tiếng Việt” vì đầy đủ thông tin hơn.

Không rút gọn thành “Âm thanh gốc (Dolby Atmos)” › “Tiếng Việt (Dolby Digital 5.1)” › “Tiếng Việt” vì không mang lại lợi ích nào rõ ràng.

Tên “Âm thanh gốc (Dolby Atmos)” không cho biết là ngôn ngữ gì

Không thể hiện rõ vai trò âm thanh gốc và fallback

Việc rút gọn “Tiếng Việt [Gốc]” thành “Âm thanh gốc” chỉ sử dụng khi không có fallback.

Nếu chưa xác định track nào là âm thanh gốc

Chỉ hiển thị “Tiếng Việt (Dolby Atmos)” › “Tiếng Việt (Dolby Digital 5.1)” › “Tiếng Việt”.

Không xác định cả ngôn ngữ, hiển thị “Âm thanh 1 (Dolby Atmos)” › “Âm thanh 2 (Dolby Digital 5.1)” › “Âm thanh 3”.

Hệ thống (như encode/transcode, packager, và player) PHẢI (MUST) dựa vào quy tắc trình bày thông tin đã quy định ở trên để hỗ trợ xác định tên track (audio hay subtitle).

Xem thêm

Dolby Atmos Speaker Setup Guides - Dolby

Table 4-2: Ví dụ một số trường hợp tên track hay gặp

Ví dụ minh họa UI của tool thực hiện transcode liên quan multiple audio tracks như sau:

Figure 4-1: Minh họa UI của tool thực hiện transcode (multiple audio tracks)

Hỗ trợ nhiều kênh âm thanh (multiple audio tracks support)

Hệ thống dùng nhiều kênh âm thanh (multiple audio tracks) để thực hiện các tính năng:

Hỗ trợ nhiều track âm thanh đa ngôn ngữ (multi-language audio tracks)

Hỗ trợ thuyết minh/lồng tiếng (voice-over and dubbed audio tracks)

Hỗ trợ nhiều track audio có bitrate khác nhau (multiple audio bitrates) và nhiều mức chất lượng khác nhau (multiple audio quality levels)

Manifest chủ yếu được thiết kế dành cho việc streaming, do đó việc khai báo thông tin chi tiết và metadata của các track có thể không được hỗ trợ đầy đủ và không được khuyến khích.

Không phải tất cả các thông tin và metadata liên quan đến track đều có thể khai báo trực tiếp trong manifest.

Thẻ EXT-X-MEDIA của HLS chỉ định tổng số kênh âm thanh qua thuộc tính CHANNELS, nhưng không cung cấp cấu hình kênh (channel layout). Nó cũng không thể trực tiếp chỉ định codec, bandwidth hay sampling rate.

Representation của DASH linh động hơn khi có các thuộc tính bandwidth, codecs, sampling rate và subtag AudioChannelConfiguration chứa thông tin cấu hình kênh. Tuy nhiên, DASH vẫn bị giới hạn ở một số thông tin này và không thể cung cấp thêm nhiều chi tiết khác.

HLS và DASH hạn chế việc khai báo thông tin về các track trong manifest và không cho phép tùy biến quá mức.

API cung cấp khả năng khai báo chi tiết hơn cho các track, như thể loại, vai trò, mà không bị ràng buộc bởi quy định, cấu trúc của manifest.

Thông tin track có thể cập nhật thường xuyên thông qua API.

Xem ví dụ cụ thể của HLS và DASH tại

Dash Reference Client 4.7.4, released Feb 20th, 2024 (dashif.org)

Examples - HTTP Live Streaming - Apple Developer

Do hạn chế của thẻ EXT-X-MEDIA không chỉ định trực tiếp codec, bandwidth hay sampling rate, nên cần:

Tách thẻ EXT-X-STREAM-INF cho từng codec audio, thay vì gộp chung các codec audio trong thuộc tính CODECS.

Dùng thuộc tính GROUP-ID, hay URI của thẻ EXT-X-MEDIA để chỉ định codec, bandwidth hoặc sampling rate nếu cần.

Ví dụ chia các group thể hiện qua giá trị của GROUP-ID

AAC-LC 48 kHz stereo @ 161 kbps với GROUP-ID=”aaclc-48-160”

AC-3 48 kHz 5.1 @ 384 kbps với GROUP-ID=”ac3-48-384”

EC-3 48 kHz 7.1 @ 768 kbps với GROUP-ID=”ec3-48-768”

Hay tương tự dùng thông qua giá trị của URI=”aaclc-48-160/audio.m3u8”

Hệ thống NÊN (SHOULD) sử dụng tên thư mục/phân đoạn (folder/segment name) cho URI ít nhất là phân chia theo audio codec. Giá trị folder/segment name theo codec được quy định như sau:

Table 4-3: Folder/segment name dùng cho URI tương ứng codec identifier

Các packager từ các nhà cung cấp khác nhau có thể có giới hạn trong việc tùy chỉnh tên thư mục hoặc phân đoạn (folder/segment name).

Cụ thể, packager thường không hỗ trợ URI với segment chứa thông tin mong muốn như codec, bandwidth, hay sampling rate kiểu aaclc-48-160.

Hay segment name của Dolby Digital Plus có thể được thể hiện dưới nhiều dạng khác nhau: ec3, ec-3, ac3, eac3, ddplus …

Vì hạn chế này của packager, cần xem xét và xử lý linh hoạt trong từng trường hợp cụ thể. Ví dụ, việc xác định EC-3 w/ Dolby Atmos (Dolby Digital Plus carry nội dung Dolby Atmos) thực hiện thông qua:

Xác định codec Dolby Digital Plus qua bất kỳ segment name nào có thể như ec3, ec-3, ac3, eac3, hoặc ddplus.

Xác định Dolby Atmos bằng thông tin bổ sung như:

CHANNELS="16/JOC" với HLS

SupplementalProperty với DASH (xem thêm SupplementalProperty descriptor)

Lưu ý HLS không sử dụng “ec+3” để chỉ Dolby Digital Plus carry nội dung Dolby Atmos.

The MP4 registration authority (mp4ra.org) lists a value of ec+3 for Enhanced AC-3 audio with JOC (Dolby Atmos). That value is not used by HLS. Instead, it uses ec-3 and marks the presence of the additional JOC content with JOC in the CHANNELS attribute of the audio rendition. The JOC must be capitalized. For example, CHANNELS="16/JOC".

Apple HLS specs appendixes | Apple Developer Documentation

Hệ thống NÊN (SHOULD) cung cấp thông tin chi tiết về các audio track thông qua API bao gồm:

Tên track (như mô tả tại [4.2 — Tên track (track names)])

Thông số kỹ thuật, ví dụ như:

Định dạng/codec

Bitrate (kbps)

Sample rate

Số kênh (channels)

Cấu hình kênh (channel layout) ví dụ 6 track/channel và layout là 5.1

Loudness (xem thêm https://en.wikipedia.org/wiki/LKFS)

True peak, đơn vị decibel True Peak (dBTP)

Vai trò (role), ví dụ như

Âm thanh gốc (original) hay bản sao (duy nhất) khi không có âm thanh gốc thực sự

Bình luận (commentary)

Lồng tiếng (dubbed)

Thuyết minh (voice-over)

Karaoke (karaoke)

Các thông tin khác nếu cần như encoder, artist, copyright

Thứ tự (hiển thị) audio tracks (audio tracks display order)

Thứ tự (hiển thị) trên player PHẢI (MUST) được thực hiện như sau:

Ưu tiên tiếng Việt (ngôn ngữ chính), luôn đặt ở vị trí đầu tiên nếu có.

Nếu có cả lồng tiếng (dubbed) và thuyết minh (voice-over) thì ưu tiên lồng tiếng

Thứ tự “Lồng tiếng” › “Thuyết minh”, thông tin ngôn ngữ tiếng Việt có thể rút gọn

Lý do lồng tiếng thường yêu cầu đầu tư công sức và chi phí nhiều hơn và được xem là một bản audio “chính thức” của phim.

Sau track âm thanh tiếng Việt thì track âm thanh gốc (và các bản sao của âm thanh gốc) sẽ được ưu tiên hiển thị. Ví dụ nếu tiếng Hàn là ngôn ngữ của âm thanh gốc thì thứ tự hiển thị là “Thuyết minh” › “Tiếng Hàn [Gốc]”.

Thứ tự hiển thị của ngôn ngữ sẽ được ưu tiên cho các ngôn ngữ có độ phổ biến cao (sau ưu tiên tiếng Việt và ngôn ngữ của âm thanh gốc).

Cụ thể ưu tiên các ngôn ngữ sau theo thứ tự “Tiếng Anh” › “Tiếng Trung” › “Tiếng Hàn” › “Tiếng Nhật” › “Tiếng Thái”.

Các ngôn ngữ còn lại nếu không nằm trong danh sách ưu tiên ở trên sẽ sắp xếp theo thứ tự alphabet của tên ngôn ngữ (trong tiếng Việt). Ví dụ “Tiếng Bồ Đào Nha” (B) › “Tiếng Pháp” (P) › “Tiếng Tây Ban Nha” (T).

Ngoài ra, liên quan đến ngôn ngữ sẽ được sắp xếp từ tổng quát đến cụ thể. Ví dụ “Tiếng Bồ Đào Nha” sẽ xếp trước “Tiếng Bồ Đào Nha (Brazil)”.

Sau việc nhóm các âm thanh gần nhau theo ngôn ngữ, việc sắp xếp thứ tự sẽ dựa vào mức chất lượng âm thanh (sắp xếp theo audio quality levels).

Cụ thể âm thanh chất lượng cao (lossless/high-quality) sẽ nằm ở đầu, sau đó đến chất lượng thấp hơn (low quality).

Ví dụ “Tiếng Hàn [Gốc] (Dolby Atmos)” › “Tiếng Hàn (Dolby Digital 5.1)” › “Tiếng Hàn”

Việc sắp xếp giúp người dùng dễ dàng nhận biết có các track âm thanh chất lượng cao.

Chất lượng âm thanh được sắp xếp ưu tiên theo thứ tự như sau immersive sound › surround sound › lossless › âm thanh stereo hoặc mono (thông thường hay fallback)

Immersive sound (âm thanh sống động) dùng các công nghệ âm thanh 3D như Dolby Atmos, còn gọi là âm thanh vòm đa chiều (từ nhiều hướng khác nhau)

Surround sound (âm thanh vòm truyền thống) là một công nghệ âm thanh tạo ra trải nghiệm đa chiều với nhiều loa xung quanh người nghe.

Âm thanh lossless là các âm thanh sử dụng công nghệ mã hóa không mất dữ liệu nhằm giữ nguyên chất lượng gốc.

Thứ tự sắp xếp audio codec cụ thể như sau:

Dolby Atmos được xem là immersive sound chất lượng cao nhất

Dolby Digital Plus w/ Atmos

Dolby Digital Plus

Dolby Digital

Lossless (FLAC/ALAC)

Codec còn lại là AAC, Vorbis/Opus

Sau audio codec (thường liên quan lossless/lossy), mức chất lượng âm thanh được xác định bởi các tính chất:

Thứ tự bitrate › sample rate › channels — Bitrate được ưu tiên đầu vì dễ xác định và phản ánh chất lượng tổng thể. Việc có nhiều kênh hoặc sample rate cao, hay có kèm dữ liệu metadata cho âm thanh đều dẫn đến bitrate cao.

Bitrate — Yếu tố quan trọng nhất trong việc xác định chất lượng âm thanh. Ví dụ cụ thể một track âm thanh bitrate 128 kbps sẽ có chất lượng thấp hơn so với một track với bitrate 320 kbps

Channels — Số lượng kênh âm thanh (như mono, stereo, hoặc surround sound). Channels có tác động trực tiếp đến trải nghiệm âm thanh.

Sample rate — Tần số mẫu cao hơn cung cấp chất lượng âm thanh tốt hơn, 48 kHz thường được sử dụng cho video. Sample rate có ý nghĩa trong việc cải thiện chi tiết âm thanh.

Nếu có 2 track có cùng các tiêu chí so sánh thì sắp xếp theo tên codec

Việc bổ sung audio track vào phía sau thường linh hoạt hơn và đảm bảo thứ tự track ít bị thay đổi.

Do nội dung PHẢI (MUST) bao gồm ít nhất một luồng âm thanh AAC (least one stream of AAC) để đảm bảo khả năng tương thích.

Track AAC (fallback) thường sẽ được thêm vào sau track âm thanh chất lượng cao ví dụ âm thanh gốc chất lượng Dolby Atmos.

Thứ tự (hiển thị) các audio tracks theo mong muốn trên PHẢI (MUST) được hỗ trợ từ encode/transcode, đến API, và các thành phần khác.

Tham khảo

Delivering premium HLS audio experiences with Bitmovin

Nếu hai track âm thanh có tên track (tự xác định) như nhau do cùng cả ngôn ngữ, vai trò và chất lượng âm thanh, đội Nội dung và Vận hành phải thực hiện thiết lập trên track thủ công để đảm bảo người dùng có thể phân biệt được.

Ví dụ, video ca nhạc có một track âm thanh AAC bình thường với nhạc và lời, cùng hai track beat karaoke AAC có chất lượng như nhau

Thông tin trong manifest thường không đủ để xác định tên track.

Nếu không xác định ngôn ngữ có thể hiển thị “Âm thanh 1/2/3”

Nhưng nếu là tiếng Việt, không thể cùng hiển thị cùng là “Tiếng Việt”.

Trường hợp tệ nhất, cùng tên mà không có thông tin từ API, tạm xử lý như sau:

Thêm suffix 1, 2 cho các item bị trùng

Tức hiển thị “Tiếng Việt 1” › “Tiếng Việt 2” › “Tiếng Việt 3”

Hoặc hệ thống PHẢI (MUST) chỉ định tên thông qua API, ví dụ “Vocal” › “Beat tone nam [Karaoke]” › “Beat tone nữ [Karaoke]”.

Hiển thị danh sách audio tracks (player)

Player sẽ ưu tiên lấy thông tin track names theo thứ tự

API cung cấp › thông tin track names dựa theo danh sách từ API trả về

Thông tin có sẵn, “trực tiếp” trong manifest › thông tin track name có sẵn trong manifest (ví dụ NAME attribute của EXT-X-MEDIA với HLS m3u8 manifest hay thông tin của AdaptationSet với DASH mpd manifest)

Xử lý theo quy tắc › xác định track names dựa trên các yếu tố như ngôn ngữ, codec, chất lượng và cấu hình âm thanh.

Lưu ý:

Nhiều player hỗ trợ DASH khác nhau, có thể chỉ hỗ trợ Label node hoặc cả label dưới dạng attribute (hay custom attribute). Mục 5.3.10 trong DASH 3rd (2019-08) ISO/IEC 23009-1:2019 quy định Label dưới dạng node, không phải attribute. Một số player thương mại lại sử dụng custom attribute (ví dụ: Bitmovin sử dụng “bitmovin:label”).

Lý do không sử dụng chỉ một bước thông tin có sẵn trực tiếp trong manifest

Thông tin trực tiếp trong manifest có thể không có, không chính xác nhưng không thể kiểm soát trong trường hợp tiếp sóng.

Thông tin trong manifest không có với những nội dung quá cũ › tạm sử dụng khi chưa transcode lại được.

API luôn cho phép cập nhật track names nhanh chóng và linh động.

Nếu có thông tin audio track names trong manifest, player sẽ thay thế (override, replace) thông tin trong manifest bằng thông tin từ API trả về:

Số lượng items từ API cần khớp với số track trong manifest.

Trường hợp (ngoại lệ) số lượng items không khớp › cần xem xét và báo lỗi warning

Nếu API trả về ít items hơn số track trong manifest, chỉ các items có trong API sẽ được sử dụng.

Ví dụ maniest có 3 tracks “Audio 1” › “Audio 2” › “Audio 3”

API trả về thông tin chỉ có 2 items “Thuyết minh” › “Tiếng Hàn [Gốc]”

Kết quả sau khi override là “Thuyết minh” › “Tiếng Hàn [Gốc]” › “Audio 3”

Nếu API trả về nhiều items hơn số track trong manifest, chỉ sử dụng số lượng tương ứng với track thực tế trong manifest.

API trả về 4 items “Thuyết minh” › “Tiếng Hàn [Gốc] (Dolby Atmos)” › “Tiếng Hàn” › “Tiếng Anh”

Nhưng maniest chỉ có 3 tracks “Vietnamese” › “Original” › “Fallback”

Kết quả sau khi override là “Thuyết minh” › “Tiếng Hàn [Gốc] (Dolby Atmos)” › “Tiếng Hàn”

Trường hợp không có cả thông tin từ API lẫn audio track names trực tiếp trong manifest, player có thể chủ động hiển thị track name theo các quy tắc quy định trong mục [4.1 — Thẻ ngôn ngữ (language tags)] và [4.2 — Tên track (track names)].

Cấu hình manifest

Việc thực hiện khai báo và tạo các nhóm audio renditions (audio rendition groups) tuân theo tiêu chuẩn:

Với HLS cụ thể HLS 2nd draft-pantos-hls-rfc8216bis-15 quy định tại section 4.4.6.1.1 (Multivariant Playlist Tags › EXT-X-MEDIA › Rendition Groups)

HLS thực hiện thông qua cơ chế audio/video demuxing với EXT-X-MEDIA tags với loại là âm thanh (TYPE=AUDIO).

Với DASH việc triển khai multiple audio tracks có thể được thực hiện thông qua AdaptationSet và Representation (xem chi tiết mục 5.3.7.2)

Liên quan đến track names xem chi tiết tại mục 5.3.10 — “Label and Group Label”, DASH 5th Ed (2022-08) ISO/IEC 23009-1:2022

Chú ý thuộc tính @label (@label attribute) không được quy định trong tiêu chuẩn DASH.

Cả HLS và DASH đều dựa vào RFC 5646 (BCP 47) để chỉ định ngôn ngữ cho các track âm thanh và phụ đề.

Việc sử dụng language tags là tùy thuộc vào nhu cầu cụ thể.

Các audio track vẫn có thể được phân biệt (bởi user) thông qua tên track (track name).

Với đặc tả HLS m3u8 manifest:

Thuộc tính ngôn ngữ (LANGUAGE audio rendition attribute) dùng chỉ định ngôn ngữ chính của một rendition âm thanh hoặc phụ đề.

Thuộc tính ngôn ngữ liên kết (ASSOC-LANGUAGE audio rendition attribute) cũng là một chuỗi chứa language tag nhưng có vai trò khác so với ngôn ngữ chính.

Khi một audio track có thuộc tính ASSOC-LANGUAGE, thuộc tính này chỉ định các phụ đề (subtitles) liên kết với audio track đó.

Điều này đặc biệt hữu ích trong các trường hợp như cùng một ngôn ngữ âm thanh nhưng khác nhau về chữ viết hoặc phương ngữ (spoken language dialect), yêu cầu các phụ đề khác nhau để phản ánh chính xác nội dung.

Ví dụ cụ thể dưới đây mô tả cách sử dụng LANGUAGE và ASSOC-LANGUAGE với HLS manifest.

Ngôn ngữ gốc là tiếng Quảng Đông (Cantonese/粵語)

Phim có bản âm thanh thuyết minh (voice-over audio) tiếng Việt

Phim có phụ đề tiếng Việt

Phim có hai phiên bản phụ đề tiếng Hoa (tiếng Trung) là

Chữ Hán giản thể (Simplified Han/簡體中文)

Và chữ Hán phồn thể (Traditional Han/繁體中文)

Giả sử user không có preferences về ngôn ngữ cũng chưa có settings về ngôn ngữ trước đó đối với nội dung này (chưa từng xem, không có previous settings):

Khi đó ngôn ngữ mặc định của âm thanh được chọn là thuyết minh tiếng Việt với DEFAULT=YES và AUTOSELECT=YES

Track âm thanh tiếng Quảng Đông được thiết lập DEFAULT=NO và AUTOSELECT=NO. Ngoài ra khi người dùng chọn audio này thì phụ đề tiếng Việt (ưu tiên) sẽ được tự động bật thông qua cài đặt ASSOC-LANGUAGE="vi".

Cấu hình EXT-X-MEDIA:TYPE=AUDIO cho audio sẽ như sau

# Thuyết minh tiếng Việt (default)

#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio/mp4a.40.2",NAME="Thuyết minh",DEFAULT=YES,AUTOSELECT=YES,LANGUAGE="vi",CHANNELS="2",URI="audio/vi/mp4a.40.2/media.m3u8"

# Tiếng Quảng Đông (âm thanh gốc)

#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio/mp4a.40.2",NAME="Tiếng Quảng Đông [Gốc]",DEFAULT=NO,AUTOSELECT=NO,LANGUAGE="zh",ASSOC-LANGUAGE="vi",CHANNELS="2",URI="audio/zh/mp4a.40.2/media.m3u8"

Cấu hình EXT-X-MEDIA:TYPE=SUBTITLES cho phụ đề (tức dạng in-manifest referenced subtitles) sẽ như sau:

# Phụ đề tiếng Việt

#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs",NAME="Tiếng Việt",DEFAULT=NO,AUTOSELECT=YES,LANGUAGE="vi",FORCED=NO,URI="subs/vi/media.m3u8"

# Phụ đề tiếng Hoa giản thể

#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs",NAME="Tiếng Trung (Giản thể)",DEFAULT=NO,AUTOSELECT=NO,LANGUAGE="zh-Hans",URI="subs/zh-Hans/media.m3u8"

# Phụ đề tiếng Hoa phồn thể

#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs",NAME="Tiếng Trung (Phồn thể)",DEFAULT=NO,AUTOSELECT=NO,LANGUAGE="zh-Hant",URI="subs/zh-Hant/media.m3u8"

Với DASH mpd manifest:

Dùng attribute language của AdaptationSet element để chỉ định ngôn ngữ.

Hỗ trợ phụ đề (subtitles & captions support)

Hệ thống PHẢI (MUST) hỗ trợ phụ đề với các yêu cầu sau:

Loại phụ đề là out-of-band và tham chiếu qua manifest (in-manifest referenced subtitles).

Phụ đề được sử dụng phải ở định dạng WebVTT.

Thứ tự (hiển thị) phụ đề (subtitles display order)

Tương tự audio track như đơn giản hơn, danh sách phụ đề được hiển thị theo thứ tự ưu tiên. Thứ tự (hiển thị) trên player PHẢI (MUST) được thực hiện như sau:

Item đầu tiên luôn là TẮT phụ đề (tương ứng với ưu tiên audio tiếng Việt)

Tiếp theo là ưu tiên phụ đề tiếng Việt (tương ứng với thứ tự âm thanh gốc bên audio)

Cuối cùng thứ tự hiển thị của ngôn ngữ sẽ được ưu tiên cho các ngôn ngữ có độ phổ biến cao.

Cụ thể ưu tiên các ngôn ngữ sau theo thứ tự “Tiếng Anh” › “Tiếng Trung” › “Tiếng Hàn” › “Tiếng Nhật” › “Tiếng Thái”.

Các ngôn ngữ còn lại nếu không nằm trong danh sách ưu tiên ở trên sẽ sắp xếp theo thứ tự alphabet của tên ngôn ngữ (trong tiếng Việt). Ví dụ “Tiếng Bồ Đào Nha” (B) › “Tiếng Pháp” (P) › “Tiếng Tây Ban Nha” (T).

Ngoài ra, liên quan đến ngôn ngữ sẽ được sắp xếp từ tổng quát đến cụ thể. Ví dụ “Tiếng Bồ Đào Nha” sẽ xếp trước “Tiếng Bồ Đào Nha (Brazil)”.

Trường hợp có hai phiên bản phụ đề cùng ngôn ngữ nhưng cách viết khác nhau như chữ Hán giản thể (Simplified Han/簡體中文/zh-Hans) và chữ Hán phồn thể (Traditional Han/繁體中文/zh-Hant) cũng áp dụng ưu tiên độ phổ biến cao cụ thể “Tiếng Trung (Giản thể)” › “Tiếng Trung (Phồn thể)”.

Hiển thị danh sách phụ đề (player)

Tương tự việc hiển thị danh sách (tên) các audio tracks, player sẽ ưu tiên lấy thông tin track names theo thứ tự

API cung cấp › thông tin track names dựa theo danh sách từ API trả về

Thông tin có sẵn, “trực tiếp” trong manifest › thông tin track names có sẵn trong manifest tương tự với audio tracks.

Xử lý theo quy tắc › xác định track names dựa vào ngôn ngữ.

Trường hợp không có cả thông tin từ API lẫn track names trực tiếp trong manifest, player có thể chủ động hiển thị track name theo các quy tắc quy định trong mục [4.1 — Thẻ ngôn ngữ (language tags)] và [4.2 — Tên track (track names)].

Cấu hình manifest

Cơ chế chọn lựa và fallback (track selection and fallback mechanism)

Cơ chế lựa chọn âm thanh/phụ đề

Việc lựa chọn audio/subtile dựa trên thông tin ngôn ngữ ưu tiên (preferred language settings). Thông tin này (hiện tại chưa có cài đặt này trên hệ thống) gồm 3 yếu tố:

Ngôn ngữ ưu tiên dành cho âm thanh (preferred audio language)

Ưu tiên một ngôn ngữ cụ thể ví dụ tiếng Việt hay tiếng Anh

Ưu tiên một ngôn ngữ của âm thanh gốc Âm thanh gốc

Ngôn ngữ ưu tiên dành cho phụ đề (preferred subtitles language)

Ưu tiên một ngôn ngữ cụ thể ví dụ tiếng Việt hay tiếng Anh

Hoặc ưu tiên TẮT phụ đề

Và BẬT/TẮT thiết lập chỉ tự động chọn phụ đề nếu ngôn ngữ âm thanh là tiếng nước ngoài (auto-enable subtitles for foreign languages only)

Mặc định, thiết lập ngôn ngữ ưu tiên (preferred language settings) cho user sẽ là:

Ngôn ngữ ưu tiên dành cho âm thanh: tiếng Việt

Ngôn ngữ ưu tiên dành cho phụ đề: tiếng Việt

Tự động chọn phụ đề (cho tiếng nước ngoài): BẬT

Việc lựa chọn audio/subtitle PHẢI (MUST) được thực hiện như sau:

Figure 4-2: Cơ chế lựa chọn audio/subtitle

Cơ chế dự phòng (fallback)

Hệ thống PHẢI (MUST) luôn chuẩn bị các track dự phòng với codec AAC cho các track âm thanh chất lượng cao, đặc biệt là âm thanh gốc (đồng thời tuân thủ như Apple HLS specs).

Hệ thống sẽ lựa chọn track âm thanh theo quy tắc đã đề ra, ưu tiên âm thanh chất lượng cao.

Khi một track audio được hệ thống lựa chọn (lần đầu) không khả dụng (tức không thể playback), hệ thống sẽ tự động chuyển sang track AAC dự phòng mà không cần thông báo cho người dùng.

Tuy nhiên, nếu người dùng chọn thủ công một track không khả dụng (chủ động chọn), hệ thống không được tự động fallback qua track khác mà PHẢI (MUST) hiển thị thông báo lỗi.

TỔ CHỨC CHUNG CỦA MANIFEST

Tổ chức rendition (rendition structuring)

Yêu cầu hệ thống PHẢI (MUST) thực hiện tổ chức rendition dựa trên codec (rendition sets based on codecs).

Mỗi codec PHẢI (MUST) có một bộ rendition riêng biệt, chứa các phiên bản bitrate và độ phân giải khác nhau của cùng mezzanine. Các rendition set nhóm theo một codec duy nhất sẽ đảm bảo việc chuyển đổi không bị lỗi và tối ưu tính tương thích của thiết bị.

Hệ thống KHÔNG ĐƯỢC (MUST NOT) sử dụng các bộ rendition có codec hỗn hợp (mixed-codec renditions).

Apple HLS specs (mục 1.23) yêu cầu nếu cung cấp nhiều codecs (như H.264, HEVC, và có hay không HDR), thì mỗi codec khác nhau NÊN (SHOULD) bao gồm tất cả các mức băng thông dự kiến. Clients KHÔNG NÊN (SHOULD NOT) bị yêu cầu phải chuyển đổi giữa các loại codec khác nhau.

Bảng dưới đây mô tả chi tiết các rendition sets và codec tương ứng, chính là encoding (bitrate) ladder của từng codec. Mỗi rendition bao gồm thông tin về độ phân giải (resolution), bitrate, và tốc độ khung hình (framerate).

Table 5-1: Tổ chức renditions cho VOD

Nhận diện thiết bị và lựa chọn playlist/manifest

Biến thể (variants), cụ thể là các adaptation sets (của các renditions), là các phiên bản nội dung khác nhau dựa trên các codec như H.264, HEVC, AV1 và VP9 (dự phòng), bao gồm cả tính năng HDR. Do không phải thiết bị nào cũng hỗ trợ tất cả các codec và HDR, cần có cơ chế lựa chọn biến thể phù hợp dựa trên khả năng của thiết bị (device detection and playlist/manifest selection).

Ngoài việc lựa chọn, hệ thống có thể điều chỉnh (manipulation) hoặc tạo mới manifest (dynamic manifest generation), nếu có thể, dựa trên thông tin thiết bị, nhằm tối ưu cho từng loại thiết bị.

Các bước thực hiện như sau:

Xác định loại ứng dụng — Dựa vào thông tin client gửi và manifest request sẽ xác định ứng dụng client là app hay web, cùng các tính năng sẽ cung cấp.

Xác định thông tin thiết bị và khả năng hỗ trợ — Xác định thông tin thiết bị (dòng thiết bị, loại thiết bị ...) cùng các khả năng hỗ trợ (device capabilities) liên quan như video/audio codecs support, HDR support, kích thước màn hình.

Lọc manifest theo loại thiết bị (by device type) — Dựa vào thông tin loại thiết bị sẽ lọc bớt các manifest không đáp ứng được. Ví dụ Apple devices sẽ về HLS manifest, không sử dụng VP9 (và hiện tại cũng không dùng AV1).

Lọc theo hệ điều hành (by OS type/version) — Ví dụ AV1 hoặc HDR có thể chỉ hoạt động trên các hệ điều hành mới.

(Tùy chọn) Lọc theo vị trí địa lý (by geographic region) — Nếu xác định được vị trí địa lý (geo location) hay các thông tin tương tự khác như ISP › hệ thống sẽ xác định CDN › sau đó xem xét ví dụ CDN đó có áp đặt giới hạn về độ phân giải và tốc độ tối đa hay không.

Lọc theo dòng thiết bị cụ thể (by device model) — Dựa vào model cụ thể (ví dụ: iPhone 15, Samsung Galaxy S23, LG webOS TV 4K) hệ thống sẽ điều chỉnh (manipulation) hay lựa chọn danh sách renditions/playlist phù hợp với khả năng của thiết bị đó. Đây là bước quan trọng nhất khi trên khả năng hỗ trợ (device capabilities) của thiết bị phần lớn sẽ được xác định tại bước này.

Lọc dựa trên lịch sử playback và các quy tắc (rules engine) — Lịch sử playback giúp điều chỉnh hay lựa chọn manifest để tránh lỗi tương thích. Nếu lịch sử playback cho thấy thiết bị không thể phát một số loại manifest (codec hoặc profile HDR cụ thể), các manifest đó sẽ không được trả về nữa trong các lần phát sau. Ngoài ra, có thể có thể đặt ra các quy tắc dựa trên hiệu suất và tương thích của thiết bị. Ví dụ, nếu lịch sử playback cho thấy thiết bị liên tục gặp sự cố với codec HEVC/H.265, manifest sẽ chuyển sang codec H.264/AVC với tính tương thích cao hơn.

Sau khi server gửi danh sách manifest đến client, quá trình playback sẽ bắt đầu.

Ưu tiên manifest cho chất lượng video/audio tốt nhất như codec cao hơn, HDR (Dolby Vision) và âm thanh chất lượng (Dolby Atmos).

Nếu client gặp lỗi tương thích phải fallback từ chất lượng cao xuống thấp, thông tin về tính tương thích sẽ được gửi về cho server.

Trong quá trình playback, client cũng liên tục gửi dữ liệu về hiệu suất và các vấn đề phát sinh đến hệ thống analytics.

Hệ thống sẽ phân tích thông tin này để đưa ra quyết định lựa chọn manifest cho các lần playback tiếp theo. Quá trình này đảm bảo chất lượng và khả năng tương thích tốt hơn dựa trên lịch sử và hiệu suất thực tế của từng thiết bị.

Figure 5-1: Cơ chế lựa chọn playlist/manifest dựa trên thông tin thiết bị

ON-DEMAND STREAMING (VOD)

Chi tiết bổ sung trong release sau của đặc tả.

LIVE STREAMING

Chi tiết bổ sung trong release sau của đặc tả.

DRM & BẢO VỆ NỘI DUNG (DRM & CONTENT PROTECTION)

Device content protection capabilities

THAM KHẢO (REFERENCES)

The Law of Journalism and Mass Communication, 7th, ISBN: 978-1544377582 (December 4, 2019)

ITU-T J.343 (2014-11)

ITU-T GSTP-IPTV-QoS (2020-04): “Performance metrics for end-to-end IPTV video quality”

RFC 2119 (1997-03) “Key words for use in RFCs to Indicate Requirement Levels”, BCP 14

APPENDIX — CONFORMANCE REQUIREMENTS/NOTATION

Các từ khóa ký hiệu tuân thủ yêu cầu bao gồm:

## Table 1

| Phiên bản Version | Ngày Date | Người đánh giá/kiểm tra Reviewed by | Lý do Reasons |
| --- | --- | --- | --- |
| 1.1 | 2024-09-22 | VuDA7 | First draft |
| 1.0 | 2024-08-24 | YenLTX | Outline |

## Table 2

| Phiên bản Version | Ngày Date | Lý do thay đổi Reason for change |
| --- | --- | --- |
| 1.1 | 2024-09-22 | Bổ sung nội dung tổng quan video streaming, thuật ngữ, đặc tả |
| Chuẩn bị bởi (prepared by): VuDA7, ThaoLTT80, YenLTX Người đánh giá/kiểm tra (reviewed by): VuDA7 Người phê duyệt (approved by): N/A Tình trạng thực hiện (implementation status): ✗ Chưa bắt đầu (not started) ✗ Đã lên kế hoạch (to do/planned) ☑ Đang thực hiện (in progess) ✗ Đã hoàn thành/chưa đưa vào sử dụng (completed/not deployed, not in use) ✗ Đã triển khai sử dụng (deployed, in use) Mô tả/tóm tắt (description/summary) Thêm [2.1— Hệ sinh thái truyền hình] Bổ sung các thuật ngữ liên quan quảng cáo (ad stitching, SSAI, SCTE-35) Bổ sung phần bảo vệ nội dung (DRM) Bổ sung đặc tả liên quan Dolby Vision và Dolby Atmos Bổ sung các phần liên quan đến cast, giao thức cast | Chuẩn bị bởi (prepared by): VuDA7, ThaoLTT80, YenLTX Người đánh giá/kiểm tra (reviewed by): VuDA7 Người phê duyệt (approved by): N/A Tình trạng thực hiện (implementation status): ✗ Chưa bắt đầu (not started) ✗ Đã lên kế hoạch (to do/planned) ☑ Đang thực hiện (in progess) ✗ Đã hoàn thành/chưa đưa vào sử dụng (completed/not deployed, not in use) ✗ Đã triển khai sử dụng (deployed, in use) Mô tả/tóm tắt (description/summary) Thêm [2.1— Hệ sinh thái truyền hình] Bổ sung các thuật ngữ liên quan quảng cáo (ad stitching, SSAI, SCTE-35) Bổ sung phần bảo vệ nội dung (DRM) Bổ sung đặc tả liên quan Dolby Vision và Dolby Atmos Bổ sung các phần liên quan đến cast, giao thức cast | Chuẩn bị bởi (prepared by): VuDA7, ThaoLTT80, YenLTX Người đánh giá/kiểm tra (reviewed by): VuDA7 Người phê duyệt (approved by): N/A Tình trạng thực hiện (implementation status): ✗ Chưa bắt đầu (not started) ✗ Đã lên kế hoạch (to do/planned) ☑ Đang thực hiện (in progess) ✗ Đã hoàn thành/chưa đưa vào sử dụng (completed/not deployed, not in use) ✗ Đã triển khai sử dụng (deployed, in use) Mô tả/tóm tắt (description/summary) Thêm [2.1— Hệ sinh thái truyền hình] Bổ sung các thuật ngữ liên quan quảng cáo (ad stitching, SSAI, SCTE-35) Bổ sung phần bảo vệ nội dung (DRM) Bổ sung đặc tả liên quan Dolby Vision và Dolby Atmos Bổ sung các phần liên quan đến cast, giao thức cast |
| 1.0 | 2024-08-24 | Bản thảo đầu tiên (first draft) |
| Chuẩn bị bởi (prepared by): ThaoLTT80, YenLTX Người đánh giá/kiểm tra (reviewed by): YenLTX Tình trạng thực hiện (implementation status): ✗ Chưa bắt đầu (not started) ☑ Đã lên kế hoạch (to do/planned) ✗ Đang thực hiện (in progess) ✗ Đã hoàn thành/chưa đưa vào sử dụng (completed/not deployed, not in use) ✗ Đã triển khai sử dụng (deployed, in use) Mô tả/tóm tắt (description/summary) Xác định cấu trúc và dàn ý (outline) cho tài liệu Xác định các yêu cầu cơ bản Nghiên cứu và liệt kê các tiêu chuẩn tham chiếu | Chuẩn bị bởi (prepared by): ThaoLTT80, YenLTX Người đánh giá/kiểm tra (reviewed by): YenLTX Tình trạng thực hiện (implementation status): ✗ Chưa bắt đầu (not started) ☑ Đã lên kế hoạch (to do/planned) ✗ Đang thực hiện (in progess) ✗ Đã hoàn thành/chưa đưa vào sử dụng (completed/not deployed, not in use) ✗ Đã triển khai sử dụng (deployed, in use) Mô tả/tóm tắt (description/summary) Xác định cấu trúc và dàn ý (outline) cho tài liệu Xác định các yêu cầu cơ bản Nghiên cứu và liệt kê các tiêu chuẩn tham chiếu | Chuẩn bị bởi (prepared by): ThaoLTT80, YenLTX Người đánh giá/kiểm tra (reviewed by): YenLTX Tình trạng thực hiện (implementation status): ✗ Chưa bắt đầu (not started) ☑ Đã lên kế hoạch (to do/planned) ✗ Đang thực hiện (in progess) ✗ Đã hoàn thành/chưa đưa vào sử dụng (completed/not deployed, not in use) ✗ Đã triển khai sử dụng (deployed, in use) Mô tả/tóm tắt (description/summary) Xác định cấu trúc và dàn ý (outline) cho tài liệu Xác định các yêu cầu cơ bản Nghiên cứu và liệt kê các tiêu chuẩn tham chiếu |

## Table 3

| AAC | : | Advanced Audio Coding Định dạng nén âm thanh lossy theo chuẩn MPEG-2/MPEG-4 |
| --- | --- | --- |
| ABR | : | Adaptive Bit Rate Thích ứng tốc độ bit (bitrate) |
| AC-3 | : | Dolby Digital Audio (Advanced Codec 3) Codec âm thanh surround phát triển bởi Dolby |
| ACR | : | Absolute Category Rating Xếp hạng chất lượng video dựa trên thang đo tuyệt đối |
| ATSC | : | Advanced Television Systems Committee (terrestrial/cable/satellite) Bộ tiêu chuẩn truyền hình kỹ thuật số tại Hoa Kỳ |
| AVC | : | Advanced Video Codec Chuẩn nén video H.264 hiệu quả cao |
| BER | : | Bit Error Ratio Tỷ lệ lỗi bit trong quá trình truyền dữ liệu |
| BSP | : | Broadband Service Provider Nhà cung cấp dịch vụ băng thông rộng |
| CAS | : | Conditional Access System Hệ thống bảo vệ nội dung số, kiểm soát truy cập |
| CBR | : | Constant Bit Rate Truyền tải dữ liệu với bitrate cố định/không thay đổi |
| CDN | : | Content Delivery Network Mạng lưới phân phối nội dung |
| CENC | : | Common Encryption Mã hóa chung để dùng với các hệ thống DRM khác nhau |
| CMAF | : | Common Media Application Format Định dạng chung để tối ưu hóa phát video trực tuyến |
| CMCD | : | Common Media Client Data Dữ liệu tiêu chuẩn giúp tối ưu hóa phân phối nội dung |
| CPE | : | Customer Premise Equipment Thiết bị đầu cuối tại nhà khách hàng |
| CRC | : | Cyclic Redundancy Check Phương pháp kiểm tra và phát hiện lỗi dữ liệu |
| CTA | : | Consumer Technology Association Hiệp hội Công nghệ Tiêu dung. Đơn vị tổ chức sự kiện như CES. |
| CW | : | Control Word or Code Word Thông tin điều khiển để giải mã nội dung trong hệ thống CAS |
| DAI | : | Dynamic Ad Insertion Chèn quảng cáo động |
| DASH (MPEG-DASH) | : | Dynamic Adaptive Streaming over HTTP Giao thức phát trực tuyến thích ứng qua HTTP |
| DBS | : | Direct Broadcast Satellite Truyền hình vệ tinh phát sóng (quảng bá) trực tiếp |
| DHCP | : | Dynamic Host Configuration Protocol Giao thức cấu hình động cho địa chỉ IP |
| DRM | : | Digital Rights Management Công nghệ bảo vệ bản quyền nội dung số |
| DTH | : | Direct to Home Truyền hình kỹ thuật số vệ tinh trực tiếp (tới nhà/tại nhà) |
| DTT | : | Digital Terrestrial Television Truyền hình mặt đất sử dụng tín hiệu kỹ thuật số |
| DTTB (như DTT) | : | Digital Terrestrial Television Broadcasting Phát sóng truyền hình mặt đất sử dụng tín hiệu kỹ thuật số |
| DTV | : | Digital Television Truyền hình kỹ thuật số, bao gồm vệ tinh, cáp, và mặt đất |
| DVB | : | Digital Video Broadcasting Chuẩn truyền hình kỹ thuật số phổ biến tại Châu Âu |
| DVB-C (cable) | : | Digital Video Broadcasting – Cable Tiêu chuẩn DVB qua mạng cáp |
| DVB-S (satellite) | : | Digital Video Broadcasting – Satellite Tiêu chuẩn DVB qua vệ tinh |
| DVB-T (terrestrial) | : | Digital Video Broadcasting – Terrestrial Tiêu chuẩn DVB mặt đất |
| DVB-T2 (terrestrial) | : | Digital Video Broadcasting – 2th generation Terrestrial Tiêu chuẩn DVB mặt đất phiên bản/thế hệ thứ 2 |
| ECM | : | Entitlement Control Message Thông điệp kiểm soát truy cập trong hệ thống CAS |
| EMM | : | Entitlement Management Message Thông điệp quản lý truy cập trong hệ thống CAS |
| EPG | : | Electronic Program Guide Hướng dẫn chương trình điện tử tức lịch phát sóng tổng hợp (điện tử) |
| eTOM | : | enhanced Telecom Operations Map Mô hình quy trình chuẩn cho hoạt động viễn thông |
| FCC | : | Federal Communications Commission Ủy ban Truyền thông Liên bang (Hoa Kỳ) |
| fMP4 | : | fragmented MP4 Phiên bản phân mảnh của định dạng MP4 |
| fps | : | frames per second Số khung hình hiển thị trên giây |
| FTTH | : | Fiber to the Home Mạng cáp quang trực tiếp đến nhà khách hàng |
| GOP | : | Group of Pictures Nhóm các khung hình trong video |
| HAS | : | HTTP Adaptive Streaming Truyền phát thích ứng qua HTTP |
| HDR | : | High Dynamic Range Dải tương phản động cao, cải thiện độ chi tiết và màu sắc |
| HEVC | : | High-Efficiency Video Coding Chuẩn nén video hiệu quả cao H.265 |
| HLS | : | HTTP Live Streaming Giao thức truyền phát video qua HTTP phát triển bởi Apple |
| IDR | : | Instantaneous Decoding Refresh Khung hình đặc biệt giúp đồng bộ hóa giải mã video |
| IPTV | : | Internet Protocol TeleVision Bộ giao thức truyền hình qua Internet |
| ISP | : | Internet Service Provider Nhà cung cấp dịch vụ Internet |
| ISDB-T | : | Integrated Services Digital Broadcasting – Terrestrial Chuẩn truyền hình số mặt đất theo ISDB phổ biến tại Nhật Bản |
| ITU | : | International Telecommunication Union Tổ chức Liên minh viễn thông quốc tế |
| ITU-T | : | International Telecommunication Union Telecommunication Standardization Sector Bộ phận tiêu chuẩn hóa của ITU |
| JIT | : | Just-in-Time Xử lý khi cần (không xử lý trước) |
| JITP | : | Just‐in‐Time packaging Đóng gói nội dung ngay khi cần/khi phát |
| LL-HLS | : | Low-Latency HLS Phiên bản HLS với độ trễ thấp |
| MBR | : | Multi-bitrate Phát nội dung với nhiều bitrate khác nhau dựa trên điều kiện mạng |
| MOS | : | Mean Opinion Score Điểm trung bình đánh giá chất lượng dịch vụ |
| MOS-AVQE | : | MOS estimated audiovisual quality |
| MOS-AVQO | : | MOS objective audiovisual quality |
| MOS-AVQS | : | MOS subjective audiovisual quality |
| MOS-VQE | : | MOS estimated video quality |
| MOS-VQO | : | MOS objective video quality |
| MOS-VQS | : | MOS subjective video quality |
| MP3 | : | MPEG-1/2 Audio Layer 3 Định dạng nén âm thanh kỹ thuật số phổ biến theo MPEG-1/2 |
| MPD | : | DASH manifest Tập tin chỉ mục chứa danh sách phát nội dung DASH |
| MPEG | : | Moving Pictures Expert Group Nhóm Chuyên gia Hình ảnh chuyển động, nhóm chuyên của ISO để phát triển các tiêu chuẩn mã hóa và nén video, hình ảnh |
| MUX | : | multiplexer  Thiết bị ghép nhiều tín hiệu thành một tín hiệu duy nhất |
| MVPD | : | Multichannel Video Programming Distributor Nhà phân phối chương trình video đa kênh (tại Hoa Kỳ) |
| NCTA | : | National Cable & Telecommunications Association Hiệp hội Truyền hình Cáp và Viễn thông Quốc gia, tổ chức đại diện cho ngành công nghiệp truyền hình cáp và viễn thông (tại Hoa Kỳ) |
| NTSC | : | National Television System Committee Ủy ban Hệ thống Truyền hình Quốc gia, cũng là một tiêu chuẩn phát sóng truyền hình analog (tại Hoa Kỳ) |
| PAYG | : | Pay-as-you-go Mô hình trả tiền/thanh toán dựa trên nhu cầu sử dụng |
| PCM | : | Pulse Code Modulation Kỹ thuật mã hóa tín hiệu âm thanh thành số |
| PDV | : | Packet Delay Variation Biến thiên (thay đổi) trễ giữa các gói tin khi truyền tải |
| PER | : | Packet Error Ratio Tỷ lệ lỗi gói tin trong quá trình truyền dữ liệu |
| PLR | : | Packet Loss Ratio Tỷ lệ mất gói tin trong quá trình truyền tải |
| PSNR | : | Peak Signal to Noise Ratio Tỷ lệ tín hiệu trên nhiễu, dùng để đo chất lượng video |
| PTD | : | Packet Transfer Delay Độ trễ truyền gói tin |
| QoE | : | Quality of Experience Chất lượng trải nghiệm (của người dùng cuối) |
| QoS | : | Quality of Service Chất lượng dịch vụ cung cấp cho khách hàng |
| RFC | : | Request For Comments Tài liệu đề xuất và tiêu chuẩn hóa công nghệ Internet |
| RMSE | : | Root Mean Square Error Sai số trung bình toàn phương, căn bậc hai của trung bình các sai số bình phương |
| SCTE | : | Society of Cable Telecommunications Engineers Tổ chức kỹ sư viễn thông cáp |
| SDI | : | Serial Digital Interface Giao diện truyền tải video số qua kết nối cáp đồng trục |
| SDR | : | Standard Dynamic Range Dải tương phản động tiêu chuẩn |
| SMPTE | : | Society of Motion Picture and Television Engineers Tổ chức tiêu chuẩn hóa ngành truyền hình và điện ảnh |
| SRC | : | Source Nguồn phát nội dung |
| SRT | : | Secure Reliable Transport Giao thức truyền tải bảo mật và tin cậy |
| SSAI | : | Server-Side Ad Insertion Công nghệ chèn quảng cáo từ phía server (máy chủ) |
| SVTA | : | Streaming Video Technology Alliance Liên minh công nghệ video phát trực tuyến |
| VBR | : | Variable Bit Rate Phương pháp nén video với bitrate thay đổi |
| VoD | : | Video on Demand Video theo yêu cầu có thể xem bất kỳ lúc nào |

## Table 4

| RFC 8216 |  | Phiên bản hiện tại HTTP Live Streaming 2nd (2024-11) tại draft-pantos-hls-rfc8216bis-15 (ietf.org) |
| --- | --- | --- |
| ISO/IEC 23009-1 |  | Phiên bản hiện tại ISO/IEC 23009-1:2022 (2022-08), “Information technology — Dynamic adaptive streaming over HTTP (DASH) — Part 1: Media presentation description and segment formats” |

## Table 5

| Loại | Đặc điểm chính | Cách tính phí | Ví dụ |
| --- | --- | --- | --- |
| Fixed recurring subscription | Thanh toán định kỳ cố định, không phụ thuộc mức độ sử dụng. | Mức phí cố định mỗi chu kỳ. | Netflix, Spotify |
| Pay-As-You-Go (PAYG) | Trả tiền theo mức sử dụng thực tế | Theo lượt, phút, dữ liệu, nội dung | Cloud storage, mobile data, pay-per-view |
| Usage-based subscription (Hybrid) | Có phí cố định + tính thêm theo mức sử dụng | Base fee + PAYG phần vượt mức hay tăng thêm | SaaS platforms |

## Table 6

| Tiêu chí | Có (✅/✗) | Giải thích / Lý do |
| --- | --- | --- |
| Truy cập có kỳ hạn? | Có/đúng: ✅ | Ví dụ: 3 ngày, 7 ngày, 1 tháng — quyền truy cập chỉ có hiệu lực trong thời gian cố định. |
| Auto-renew? | ✗ | Không có cơ chế auto-renew, mang tính sự kiện nên chỉ xảy ra một lần. |
| Có trạng thái thuê bao? | ✗ | Không được coi là “thuê bao”. |
| Có billing cycle? | ✗ | Không có billing cycle, chỉ là giao dịch một lần. |
| Tính phí một lần, hết hạn là thôi? | Có/đúng: ✅ | Đúng logic của PAYG / pass – trả tiền một lần, hết hạn thì dừng truy cập. |
| Tính chất sử dụng | Gắn với sự kiện, nội dung cụ thể, ngắn hạn | Ví dụ: tournament access pass, daily/weekly pass |

## Table 7

| Yếu tố | Post-production | Live production |
| --- | --- | --- |
| Thời gian | Linh hoạt, dài | Rất hạn chế, theo thời gian thực |
| Công cụ | Phần mềm chỉnh sửa chuyên dụng, máy tính cấu hình cao | Phần mềm phát sóng trực tiếp, thiết bị chuyên dụng (switcher, mixer âm thanh, camera...) |
| Quy trình | Nhiều giai đoạn: thu thập, chỉnh sửa, thêm hiệu ứng, xuất bản | Ít giai đoạn hơn, sẽ không có chỗ cho sai lầm hoặc sửa chữa khi đã phát sóng. |

## Table 8

| Độ phân giải/kích thước khung hình  (resolution) | Bitrate chưa nén (uncompressed bitrate) |
| --- | --- |
| 1280 × 720 (720p) | ~ 1.5 Gbps |
| 1920 × 1080 (1080p) | ~ 3 Gbps |
| 3180 × 2160 (2160p or 4K) | ~ 12 Gbps |

## Table 9

| Bậc (rung/layer) | Độ phân giải (resolution w × h 16:9) | Bitrate H.264/AVC (kbps) | Tốc độ khung hình (frame rate) |
| --- | --- | --- | --- |
| Rung 1 | 1920 × 1080 (1080p) | 7800 | Same as source |
| Rung 2 | 1920 × 1080 (1080p) | 6000 | Same as source |
| Rung 3 | 1280 × 720 (720p) | 4500 | Same as source |
| Rung 4 | 1280 × 720 (720p) | 3000 | Same as source |
| Rung 5 | 640 × 360 (360p) | 365 | ≤ 30 fps |

## Table 10

| Video codec (codec name) | Profile | Level | Full name | Codec string |
| --- | --- | --- | --- | --- |
| H.264/AVC  (avc1) | Baseline (42) | 3.1 (1F) | AVC constrained BP @ L3.1 | avc1.42e01f |
| H.264/AVC  (avc1) | Main (4D) | 3.1 (1F) | AVC constrained MP @ L3.1 | avc1.4d401f |
| H.264/AVC  (avc1) | High (64) | 3.1 (1F) | AVC HP @ L3.1 | avc1.64001f |
| H.264/AVC  (avc1) | High (64) | 4.0 (28) | AVC HP @ L4.0 | avc1.640028 |
| H.264/AVC  (avc1) | High (64) | 4.1 (29) | AVC HP @ L4.1 | avc1.640029 |
| H.264/AVC  (avc1) | High (64) | 4.2 (2A) | AVC HP @ L4.2 | avc1.64002a |
| HEVC/H.265  (hvc1) | Main | 4.2 | HEVC Main Profile @ L4.2 Main Tier (or Main@L4.2@Main) | hvc1.1.4.L126.B0 |
| HEVC/H.265  (hvc1) | Main 10 | 4.1 | HEVC M10P @ L4.1 MT | hvc1.2.4.L123.B0 |
| HEVC/H.265  (hvc1) | Main 10 | 5.0 | HEVC M10P @ L5.0 MT | hvc1.2.4.L150.B0 |
| HEVC/H.265  (hvc1) | Main 10 | 5.1 | HEVC M10P @ L5.1 MT | hvc1.2.4.L153.B0 |
| AV1 (av01) | Main | 3.0 | AV1 8-bit MP @ L3 MT | av01.0.04M.08 |
| AV1 (av01) | Main | 3.0 | AV1 10-bit MP @ L3 MT | av01.0.04M.10 |
| AV1 (av01) | Main | 4.1 | AV1 8-bit MP @ L4.1 MT | av01.0.09M.08 |
| VP9 (vp09) | Profile 0 | 5.0 | VP9 8-bit, Profile 0 @ L5.0 | vp09.00.50.08 |
| VP9 (vp09) | Profile 2 | 5.1 | VP9 10-bit, Profile 2 @ L5.1 | vp09.02.51.10 |
| Dolby Vision HEVC-based (dvh1) | Profile 5 | Level 1 | Dolby Vision Profile 5 (10-bit HEVC), L1 (720p24) | dvh1.05.01 |
| Dolby Vision HEVC-based (dvh1) | Profile 5 | Level 6 | Dolby Vision Profile 5 (10-bit HEVC), L6 (2160p24 tức 3840 × 2160 @ 24 fps hay 4K × 2K @ 24 fps) | dvh1.05.06 |
| Dolby Vision HEVC-based (dvh1) | Profile 8 | Level 6 | Dolby Vision Profile 8 (10-bit HEVC), L6 | dvh1.08.06 |
| Dolby Vision HEVC-based (dvh1) | Profile 8 | Level 7 | Dolby Vision Profile 8 (10-bit HEVC), L7 (2160p24) | dvh1.08.07 |
| Dolby Vision HEVC-based (dvh1) | Profile 8 | Level 9 | Dolby Vision Profile 8 (10-bit HEVC), L9 (2160p24) | dvh1.08.09 |

## Table 11

| Video codec (codec name) | Video codec (codec name) | Codec string |
| --- | --- | --- |
| MPEG-4 audio | AAC-LC | mp4a.40.2 |
| MPEG-4 audio | HE-AAC | mp4a.40.5 |
| MPEG-4 audio | HE-AAC v2 | mp4a.40.29 |
| MPEG-1/2 Audio Layer III (MP3) | MPEG-1/2 Audio Layer III (MP3) | mp3 |
| Dolby Digital (AC-3) | Dolby Digital (AC-3) | ac-3 |
| Dolby Digital Plus (E-AC-3 hay EC-3) | Dolby Digital Plus (E-AC-3 hay EC-3) | ec-3 |
| Free Lossless Audio Codec (FLAC) | Free Lossless Audio Codec (FLAC) | fLaC |
| Opus | Opus | opus |
| Vorbis | Vorbis | vorbis |
| Pulse-Code Modulation (PCM) | Pulse-Code Modulation (PCM) | pcm |
| Apple Lossless | Apple Lossless | alac |

## Table 12

| Codec cơ sở (base type) | Tên codec (codec name) | Notes (ghi chú) |
| --- | --- | --- |
| ac-3 | AC-3 audio |  |
| alac | Apple Lossless |  |
| avc1 | H.264 (Advanced Video Coding) |  |
| avc3 | H.264 (Advanced Video Coding) | Use not recommended |
| dvh1 | Dolby Vision (based on hvc1) tức HEVC-based Dolby Vision |  |
| dvhe | Dolby Vision (based on hev1) | Use not recommended |
| dav1 | Dolby Vision (based on avc1) tức AV1-based Dolby Vision |  |
| ec-3 | Enhanced AC-3 audio |  |
| fLaC | Free Lossless Audio Codec |  |
| hev1 | HEVC (High-Efficiency Video Coding) | Use not recommended |
| hvc1 | HEVC (High-Efficiency Video Coding) |  |
| mjpg | JPEG image sequence | Limited use |
| mp4a | MPEG-4 audio |  |
| stpp | Subtitles (Timed Text) |  |
| wvtt | WebVTT data |  |
| ac-3 | Dolby AC-3 audio |  |
| ac-4 | Dolby AC-4 audio |  |
| alac | Apple Lossless |  |

## Table 13

| Codec/tính năng (codec/feature) | VOD | Live | Ghi chú (notes) |
| --- | --- | --- | --- |
| H.264/AVC | ✅ | ✅ |  |
| HEVC/H.265 (SDR) | ✅ | ✅ |  |
| HEVC/H.265 (HDR) | ✅ | ✅ |  |
| VP9 | ✅ |  | Không dùng trên thiết bị Apple, mục 1.1, HLS authoring specs, video content chỉ dùng H.264/AVC, HEVC/H.265, Dolby Vision, hay AV1 |
| AV1 | ✅ |  |  |
| Dolby Vision | ✅ | ✅ |  |

## Table 14

|  | H.264/AVC | HEVC/H.265 | VP9 | AV1 |
| --- | --- | --- | --- | --- |
| Resolution |  |  |  |  |
| Input frame rate |  |  |  |  |
| Color space |  |  |  |  |
| Profile |  |  |  |  |
| Level |  |  |  |  |
| Video mode |  |  |  |  |
| Video bitrate |  |  |  |  |
| Peak video bit rate | 1.5x average | 1.5x average | 1.5x average | 1.5x average |
| Key frame interval (I-frame interval) |  |  |  |  |
| HDR support |  |  |  |  |

## Table 15

|  | H.264/AVC | HEVC/H.265 | VP9 | AV1 |
| --- | --- | --- | --- | --- |
| Mobile devices | Mobile devices | Mobile devices | Mobile devices | Mobile devices |
| Android | ✅ | ✅  (limited, Android 5+, MP @ 3.0) | ✅ | ✅ (Android 10+) |
| Apple (iOS/iPadOS) | ✅ (MP/HP @ 4.2) | ✅  (iOS 11+) | ✗ | ✅  (limited) |
| Samsung | ✅ | ✅  (limited) | ✅ | ✅ |
| Smart TVs | Smart TVs | Smart TVs | Smart TVs | Smart TVs |
| Samsung | ✅ (2018+, MP/HP @ 5.1) | ✅ (2018+, M10P @ 5.1) | ✅ (2018+, webm) | ✅ (premium, 2020+, webm) |
| LG webOS | ✅ (webOS 3+, MP/HP @ 5.1) | ✅ (webOS 3.5+, M10P @ 5.1) | ✅ (UHD 4K, mkv) | ✅ (webOS 5+) |
| Android TV | ✅ (Android 5+) | ✅ (Android 5+, MP @ 4.1) | ✅ (webm) | ✅ (2020+) |
| Sony | ✅ | ✅ | ✅ (UHD 4K, YouTube app) | ✅ (premium UHD 4K/8K HDR, 2021+) |
| TCL | ✅ | ✅ | ✅ (6-series, 8-Series) | ✅ (ATV 2021+) |
| Panasonic | ✅ | ✅ | ✅ (UHD 4K, 2021+) | ✅ (premium UHD 4K HDR, 2021+) |
| Web browsers (desktop/PC/laptop) | Web browsers (desktop/PC/laptop) | Web browsers (desktop/PC/laptop) | Web browsers (desktop/PC/laptop) | Web browsers (desktop/PC/laptop) |
| Google Chrome | ✅ | ✅ (partial, H/W dependency) | ✅ | ✅ |
| Microsoft Edge | ✅ | ✅ (partial, H/W dependency) | ✅ (2024+) | ✅ |
| Safari | ✅ | ✅ (2024+) | ✅ (partial, H/W dependency, 2024+) | ✅ (partial, H/W dependency, 2024+) |
| Mozilla Firefox | ✅ | ✗ | ✅ | ✅ |
| Opera | ✅ | ✗ | ✅ | ✅ |
| Mobile browsers (desktop/PC/laptop) | Mobile browsers (desktop/PC/laptop) | Mobile browsers (desktop/PC/laptop) | Mobile browsers (desktop/PC/laptop) | Mobile browsers (desktop/PC/laptop) |
| Android browser | ✅ | ✅ (partial, H/W dependency) | ✅ (H/W dependency, 2024+) | ✅ (2024+) |
| Samsung Internet | ✅ | ✅ | ✅ | ✅ |
| Chrome (Android) | ✅ | ✅ (partial, H/W dependency) | ✅ | ✅ |
| Firefox (Android) | ✅ | ✗ |  |  |
| Safari (iOS/iPadOS) | ✅ | ✅ (11+) | ✅ (partial, H/W dependency, 18.1+) | ✅ (partial, H/W dependency, 2024+) |
| Edge (Android/iOS/iPadOS) | ✅ | ✅ (partial, H/W dependency) | ✅ | ✅ |
| Opera Mobile (Android/iOS/iPadOS) | ✅ | ✗ | ✅ | ✅ |

## Table 16

| Technology | Dolby Vision | HDR10+ | HDR10 | HLG |
| --- | --- | --- | --- | --- |
| Codec | HEVC/H.265 | HEVC/H.265 | HEVC/H.265 | HEVC/H.265 |
| Transfer function (OETF) | PQ (in most profiles) HLG (in profile 8.4) | PQ  (SMPTE ST 2084) | PQ  (SMPTE ST 2084) | HLG |
| Metadata | Dynamic  (profile 8.4) | Dynamic | Static | None |
| Bit depth | 10-bit or 12-bit | 10-bit | 10-bit | 10-bit |
| Peak luminance / brightness (common) | 4,000 nits | 1,000 – 4,000 nits | 1,000 nits | 1,000 nits |
| Backward compatibility | Tùy thuộc profile và compatibility level: None SDR HDR10 HLG | HDR10 | None | SDR nhưng hỗ trợ Rec. 2020  (ví dụ như non-HDR 4K TV) |
| Licensing | Proprietary and license | Rotalty-free | Rotalty-free | Rotalty-free |

## Table 17

| Codec/tính năng (codec/feature) | VOD | Live | Ghi chú (notes) |
| --- | --- | --- | --- |
| AAC (AAC-LC/HE-AAC v1/2) | ✅ | ✅ |  |
| MP3 |  |  | Không hỗ trợ, thay thế bằng AAC |
| Dolby Digital (AC-3) | ✅ |  |  |
| Dolby Digital Plus (E-AC-3 hay EC-3) | ✅ |  |  |
| Dolby Digital Plus (EC-3)  with Dolby Atmos | ✅ | ✅ | Chỉ dùng EC-3 w/ Dolby Atmos, play natively với Dolby Atmos spatial audio mode |
| Vorbis | ✅ |  | Chỉ dùng với web browser |
| Opus | ✅ |  | Chỉ dùng với web browser |
| FLAC | ✅ |  |  |
| Apple Lossless (ALAC) | ✅ |  | Dùng cho thiết bị Apple |
| PCM (LPCM) | ✅ |  |  |

## Table 18

| Manifest format | Container (output) | Supported | Video codecs | Audio codecs | Ghi chú (notes) |
| --- | --- | --- | --- | --- | --- |
| DASH | fMP4 | ✅ | Video: H.264/AVC HEVC/H.265 w/ HDR-10 AV1 | Audio: AAC AC-3/EC-3 EC-3 w/ Dolby Atmos | Demuxed streams only |
| DASH | CMAF | ✅ | Video: H.264/AVC HEVC/H.265 w/ HDR-10 AV1 | Audio AAC AC-3/EC-3 EC-3 w/ Dolby Atmos | Xem xét AV1 dùng với WebM |
| DASH | WebM | ✅ | Video: VP9 | Audio: Vorbis/Opus | Demuxed streams only VP9 (dự phòng) chủ yếu chỉ dùng với WebM |
| DASH | MPEG-TS | ✗ | Not applicable | Not applicable | No support planned |
| DASH | Audio-only |  | Not applicable | Audio AAC AC-3/EC-3 EC-3 w/ Dolby Atmos |  |
| HLS | fMP4 | ✅ | Video: H.264/AVC HEVC/H.265 w/ HDR-10 | Audio: AAC AC-3/EC-3 EC-3 w/ Dolby Atmos ALAC/FLAC | Mục 1.5, Apple HLS specs yêu cầu HEVC phải dùng fMP4 Mục 2.25, Apple HLS specs yêu cầu ALAC/FLAC phải dùng fMP4 |
| HLS | MPEG-TS | ✅ | Video: H.264/AVC (up to HP @ 4.1) | Audio: AAC AC-3/EC-3 EC-3 w/ Dolby Atmos | Mục 1.3a, Apple HLS specs yêu cầu H.264/AVC nên ≤ HP @ 4.1 |
| HLS | CMAF | ✅ | Video: H.264/AVC HEVC/H.265 w/ HDR-10 AV1 | Audio: AAC AC-3/EC-3 EC-3 w/ Dolby Atmos | Mục 1.6a, Apple HLS specs yêu cầu HEVC nên ≤ M10P @ 5.1 MT HLS/CMAF + FairPlay (gồm HEVC) chỉ hỗ trợ từ iOS 11+ (2017) |
| HLS | Elementary stream/audio-only | ✅ | Not applicable | Audio: ADTS (AAC) PCM | No container (elementary audio stream) với audio-only content |

## Table 19

| Codec | CODECS attribute | SUPPLEMENTAL-CODECS attribute | VIDEO-RANGE attribute |
| --- | --- | --- | --- |
| Dolby Vision 8.4 | hvc1.2.4.L153.b0 | dvh1.08.07/db4h | HLG |
| Dolby Vision 8.1 | hvc1.2.4.L150 | dvh1.08.06/db1p | PQ |
| Dolby Vision 10.4 | av01.0.13M.10.0.112 | dav1.10.09/db4h | HLG |
| AV1 w/ HDR10+ | av01.0.05M.10.0.112 | av01.0.05M.10.0.112/cdm4 | PQ |

## Table 20

| Protocols | FairPlay | Widevine (Modular) | PlayReady | CENC | ClearKey |
| --- | --- | --- | --- | --- | --- |
| HLS | ✅ | ✅ | ✗ | ✅ | ✗ |
| DASH | ✗ | ✅ | ✅ | ✅ | ✅ |

## Table 21

| Protocols | FairPlay | Widevine (Modular) | PlayReady | CENC | ClearKey |
| --- | --- | --- | --- | --- | --- |
| Smart TV | Smart TV | Smart TV | Smart TV | Smart TV | Smart TV |
| Android TV |  |  |  |  |  |
| Samsung Tizen |  |  |  |  |  |
| LG webOS |  |  |  |  |  |
|  |  |  |  |  |  |
| Mobiles | Mobiles | Mobiles | Mobiles | Mobiles | Mobiles |
| Android |  |  |  |  |  |
| iOS |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
| Web browsers | Web browsers | Web browsers | Web browsers | Web browsers | Web browsers |
|  |  |  |  |  |  |

## Table 22

| Duration (video content) | Frame interval (giây) | Số frames (ước tính) |
| --- | --- | --- |
| ≤ 15 phút | 4 giây | ≤ 15 × 60 ÷ 4 = 225 |
| 15 phút < duration ≤ 30 phút | 7 giây | 128 - 257 frames |
| 30 phút < duration ≤ 60 phút | 10 giây | 180 - 360 frames |
| 60 phút < duration ≤ 90 phút | 15 giây | 240 - 360 frames |
| > 90 phút | 20 giây | 270+ frames |

## Table 23

| Tên track (track name) | Thẻ ngôn ngữ  (language tag) | Ngôn ngữ chính  (primary language) | Mở rộng  (extlang) | Hệ chữ viết (script) | Khu vực  (region) | Âm thanh/phụ đề |
| --- | --- | --- | --- | --- | --- | --- |
| Tiếng Anh | en | en | – | – | – | both |
| Tiếng Anh (Mỹ) | en-US | en | – | – | US | audio |
| Tiếng Anh (Anh) | en-UK | en | – | – | UK | audio |
| Tiếng Tây Ban Nha | es | es | – | – | – | both |
| Tiếng Pháp | fr | fr | – | – | – | both |
| Tiếng Pháp (Canada) | fr-CA | fr | – | – | CA | audio |
| Tiếng Nhật | ja | ja | – | – | – | both |
| Tiếng Nhật (Romaji) | ja-Latn | ja | – | Latn | – | script |
| Tiếng Hàn | ko | ko | – | – | – | both |
| Tiếng Hàn (Romaja) | ko-Latn | ko | – | Latn | – | script |
| Tiếng Hàn (Hangul) | ko-Hang | ko | – | Hang | – | script |
| Tiếng Thái | th | th | – | – | – | both |
| Tiếng Trung | zh | zh | – | – | – | both |
| Tiếng Quan Thoại | zh-cmn | zh | cmn | – | – | audio |
| Tiếng Quảng Đông | zh-yue | zh | yue | – | – | audio |
| Tiếng Trung (Giản thể) | zh-Hans | zh | – | Hans | – | script |
| Tiếng Trung (Phồn thể) | zh-Hant | zh | – | Hant | – | script |
| Tiếng Việt | vi | vi | – | – | – | both |
| Thuyết minh | vi-x-vo | vi | – | – | – | audio |
| Lồng tiếng | vi-x-dubbed | vi | – | – | – | audio |

## Table 24

| Tên hiển thị (track name) | Loại track (type) | Mô tả (description) |
| --- | --- | --- |
| Lồng tiếng Tiếng Hàn [Gốc] (Dolby Digital Plus 7.1) Tiếng Hàn (Dolby Digital 5.1)  Tiếng Hàn | Audio | Lồng tiếng tiếng Việt mono, codec như AAC. Âm thanh gốc, Dolby Digital Plus 7.1 AC-3 fallback không hỗ trợ EC-3 AAC fallback không hỗ trợ Dolby |
| Tiếng Việt [Gốc] (Dolby Atmos) Tiếng Việt (Dolby Digital 5.1)  Tiếng Việt | Audio | Âm thanh gốc, Dolby Atmos AC-3 fallback không hỗ trợ Atmos AAC fallback không hỗ trợ Dolby |
| Thuyết minh Tiếng Hàn [Gốc] (Dolby Atmos) Tiếng Hàn | Audio | Thuyết minh tiếng Việt mono, codec như AAC  Âm thanh gốc, Dolby Digital Plus w/ Dolby Atmos Track âm thanh fallback AAC mono |
| Âm thanh 1 (Dolby Atmos) Âm thanh 2 (Dolby Digital 5.1) Âm thanh 3 | Audio | Không xác định (hoặc không có) ngôn ngữ, không xác định track âm thanh gốc. |
| Tiếng Hàn [Gốc] (FLAC) | Audio | Âm thanh gốc, lossless FLAC, mono hay stereo |
| Tiếng Hàn [Gốc] (5.1) | Audio | Âm thanh surround sound AAC 5.1 |
| Tiếng Hàn [Gốc] | Audio | Âm thanh gốc, mono hay stereo codec AAC |
| Tiếng Hàn (320 kbps) Tiếng Hàn (128 kpbs) | Audio | Âm thanh mono hay stereo, codec như AAC, 320 kbps và 128 kpbs, thông số khác giống nhau |
| Tiếng Hàn (FLAC 96 kHz) Tiếng Hàn (FLAC 48 kHz) | Audio | Âm thanh mono hay stereo, codec FLAC, sampling rate 96 kHz và 48 kHz, thông số khác giống nhau |
| Tiếng Quan Thoại Tiếng Quảng Đông | Audio | Tiếng phổ thông Trung Quốc (Mandarin) và tiếng Quảng Đông (Cantonese, như ở Hồng Kông), không có gì đặc biệt, âm thanh mono xài codec như AAC |
| Tiếng Trung (Giản thể) Tiếng Trung (Phồn thể) | Subtitles | Phụ đề tiếng Trung giản thể và phụ đề tiếng Trung phồn thể |

## Table 25

| Codec identifiers  (tag string) | Tên đầy đủ (long name) | Giá trị cho URI (folder/segment name) | Ghi chú (notes) |
| --- | --- | --- | --- |
| mp4a.40.2 | AAC-LC  (Low Complexity AAC) | aaclc |  |
| mp4a.40.5 | HE-AAC v1  (High-Efficiency AAC v1) | aache |  |
| mp4a.40.29 | HE-AAC v1  (High-Efficiency AAC v2) | aachev2 |  |
| ac-3 | AC-3  (Dolby Digital) | ac3 |  |
| ec-3 | EC-3  (Dolby Digital Plus) | ec3 | Bao gồm cả EC-3 w/ Dolby Atmos. Với HLS, JOC content được chỉ định qua CHANNELS attribute ví dụ CHANNELS=”16/JOC” |
| ac-4 | Dolby AC-4 | ac4 | Codec base type. Xem thêm thông tin tại HTTP Live Streaming playlist files with Dolby AC-4 |
| fLaC | FLAC (Free Lossless Audio Codec) | flac |  |
| alac | ALAC (Apple Lossless Audio Codec) | alac |  |
| vorbis | Vorbis | vorbis |  |
| opus | Opus | opus |  |
| mp3 | MP3 (MPEG-1/2 Audio Layer III) | mp3 |  |

## Table 26

| Rendition # | Độ phân giải (resolution w × h 16:9) | Tốc độ bit (bitrate) | Tốc độ khung hình (framerate) | Ghi chú (notes) |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## Table 27

| PHẢI (MUST) |  | Từ này, hoặc các thuật ngữ "BẮT BUỘC (REQUIRED)" hoặc "SẼ PHẢI (SHALL)", có ý nghĩa là định nghĩa của một đặc tả yêu cầu không thể thiếu.  This word, or the terms "REQUIRED" or "SHALL", mean that the definition is an absolute requirement of the specification. |
| --- | --- | --- |
| KHÔNG ĐƯỢC (MUST NOT) |  | Cụm từ này, hoặc cụm từ "SẼ KHÔNG ĐƯỢC (SHALL NOT)", có ý nghĩa là định nghĩa của một đặc tả yêu cầu cấm đoán tuyệt đối.  This phrase, or the phrase "SHALL NOT", mean that the definition is an absolute prohibition of the specification. |
| NÊN (SHOULD) |  | Cụm từ này, hoặc cụm từ "KHUYẾN NGHỊ (RECOMMENDED)", nghĩa là có thể tồn tại những lý do hợp lý trong các hoàn cảnh cụ thể để bỏ qua một yêu cầu cụ thể. Tuy nhiên, trước khi quyết định, tức không theo khuyến nghị mà chọn một hướng đi khác, cần phải hiểu và cân nhắc kỹ lưỡng về các hệ quả có thể xảy ra.  This word, or the adjective "RECOMMENDED", mean that there may exist valid reasons in particular circumstances to ignore a particular item, but the full implications must be understood and carefully weighed before choosing a different course. |
| KHÔNG NÊN (SHOULD NOT) |  | Cụm từ này, hoặc cụm từ "KHÔNG KHUYẾN NGHỊ (NOT RECOMMENDED)", nghĩa là có thể tồn tại những lý do hợp lý trong các hoàn cảnh cụ thể để chấp nhận hoặc thậm chí lựa chọn có thể mang lại lợi ích. Tuy nhiên, trước khi quyết định lựa chọn, đặc biệt khi hành động này ngược lại với khuyến nghị không nên thực hiện, cần phải hiểu và cân nhắc kỹ lưỡng về các hệ.  This phrase, or the phrase "NOT RECOMMENDED" mean that there may exist valid reasons in particular circumstances when the particular behavior is acceptable or even useful, but the full implications should be understood and the case carefully weighed before implementing any behavior described with this label. |
| CÓ THỂ (MAY) |  | Cụm từ này, hoặc cụm từ "TÙY CHỌN (OPTIONAL)", nghĩa là một mục có thể được lựa chọn nhưng không bắt buộc. Một nhà cung cấp có thể chọn bao gồm mục này do yêu cầu từ thị trường cụ thể hoặc để cải thiện sản phẩm, trong khi nhà cung cấp khác có thể bỏ qua. Một triển khai/cài đặt không bao gồm một tùy chọn cụ thể PHẢI chuẩn bị để tương tác với một triển khai/cài đặt khác có bao gồm tùy chọn đó, mặc dù có thể với chức năng giảm đi. Tương tự, một triển khai/cài đặt bao gồm một tùy chọn cụ thể PHẢI chuẩn bị để tương tác với một triển khai/cài đặt khác không bao gồm tùy chọn đó (ngoại trừ những tính năng đặc biệt mà tùy chọn đó cung cấp).  This word, or the adjective "OPTIONAL", mean that an item is truly optional.  One vendor may choose to include the item because a particular marketplace requires it or because the vendor feels that it enhances the product while another vendor may omit the same item. An implementation which does not include a particular option MUST be prepared to interoperate with another implementation which does include the option, though perhaps with reduced functionality. In the same vein an implementation which does include a particular option MUST be prepared to interoperate with another implementation which does not include the option (except, of course, for the feature the option provides). |
