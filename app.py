import streamlit as st
import Xuly
import RandomInput as ran
def chuanhoa(PTH:str):
    group=[]
    handle1=PTH.strip().split(",")      #tách các pth ra
    for pth in handle1:     
        group.append(Xuly.phuthuocham(pth.strip().split(" ")[0],pth.strip().split(" ")[1]))  #tách vế trái vế phải
    return group

st.title("Tìm Khóa Cho 1 Quan hệ")

page=st.sidebar.selectbox("Chọn cách nhập PTH:",["Nhập Thủ Công","Nhập Bằng File","Tạo Ngẫu Nhiên"])
if page=="Nhập Thủ Công":
    name = st.text_input("Quan Hệ")
    st.markdown("---")
    PTH=st.text_input("Phụ Thuộc Hàm:",help="2 vế cách nhau bằng dấu cách. mỗi PTH cách nhau bằng dấu phẩy (,)")
    st.markdown("---")
    PTH=Xuly.chuanhoa(PTH.upper())
    run = st.button("Run")
    init=True
 


elif page=="Nhập Bằng File":
    input=st.text_input("Xin hãy nhập tên file",help="lưu ý:nhớ để file vào folder UMA_ENVI và đúng định dạng")
    st.markdown("---")
    st.write("Dòng Đầu file là Quan Hệ")
    st.write("Dòng Sau của file là các PTH")
    st.markdown("---")
    data=Xuly.docfile(input)
    if data==0:
        st.error("File Không hợp lệ hoặc chưa được nhập")
    else: 
        name=data[0]
        PTH=data[1]
    run = st.button("Run")
    init=True
else:
    number=st.number_input("Số lượng quan hệ muốn tạo",1)
    init=st.button("Tạo PTH và quan hệ")
    if init:
        st.markdown("---")
        PTH=[]
        st.write("Quan Hệ:")
        name=ran.RandQuanHe()
        st.write(name)
        st.markdown("---")
        st.write("Phụ thuộc hàm:")
        for i in range(0,number):
            PTH.append(ran.RandPTH(name))
        view=str(set(PTH)).strip("{").strip("}")
        st.write(view)
    run=True

if run or init:
    st.markdown("---")
    try:
        value=Xuly.findkey(name,PTH)
        st.success(f"Khóa của Quan hệ này là: {value}")
    except Exception:
        st.write("Xin hãy nhập chính xác Quan hệ và các PTH")

st.markdown("---")