FROM python:3.10.8-slim-buster

RUN python -m pip install gunicorn flask numpy pandas requests joblib==0.11 numpy scipy matplotlib ipython jupyter pandas sympy nose ibm_watson_machine_learning==1.0.253 ibm-watson-openscale==3.0.24

EXPOSE 8080

WORKDIR /workspace

COPY app.py /workspace

CMD ["python", "app.py"]
