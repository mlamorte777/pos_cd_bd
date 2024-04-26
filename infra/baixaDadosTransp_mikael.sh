#!/bin/bash

# Este exemplo baixa os dados dos cinco primeiros dias de um determinado mês e ano
# que são passados como parâmetros para o script
# Um exemple de execução do script é: ./baixaDadosTransp.sh 05 2015

# Indicando qual o endereço do site
siteDownload="https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/despesas"

# Variáveis que indicam os dias do mês, mês e ano da busca
inicioPeriodo=$1
fimPeriodo=$2
mes=$3
ano=$4

# Diretórios que serão utilizados para baixar os dados e processá-los
dataDir="./dados"
tmpDir="./tmp"

# Cria diretório
mkdir -p $dataDir
mkdir -p $tmpDir

# Executa o for para cada dia (inicio e fim) do período
for dia in $(seq -f "%02g" $inicioPeriodo $fimPeriodo); do
  zipFile=$ano$mes$dia'_Despesas.zip'

  # O comando wget vai baixar o arquivo zip com os dados do site
  echo -n "Baixando arquivo $zipFile ..."
  wget "$siteDownload/$zipFile" -P $tmpDir 2> /dev/null
  echo "OK"

  # Aqui os dados são descompactados nos diretórios temporários
  echo -n "Descompactando arquivo $zipFile ..."
  unzip -o $tmpDir/$zipFile '*Despesas_Empenho.csv' -d $tmpDir > /dev/null
  unzip -o $tmpDir/$zipFile '*Despesas_Pagamento.csv' -d $tmpDir > /dev/null 
  echo "OK"

  # Remove a primeira linha do cabeçalho
  if [ "$dia" -gt "$inicioPeriodo" ]; then
    echo -n "Linha do cabeçalho retirada"
    sed -i '1d' "${tmpDir}/${ano}${mes}${dia}_Despesas_Empenho.csv"
    sed -i '1d' "${tmpDir}/${ano}${mes}${dia}_Despesas_Pagamento.csv"
    echo "OK"
  fi
  primeiro_arquivo=false
  echo OK

  # Arquivo zip é removido
  echo -n "Removendo arquivo $zipFile ..."
  rm -f "$zipFile"
  echo "OK"
  
done

# Concatena os arquivos de despesas de empenho
echo -n "Concatenando os arquivos de Despesas Empenho..."
tail -q -n +2 "$tmpDir"/*_Despesas_Empenho.csv > "$dataDir/${ano}${mes}${inicioPeriodo}-${fimPeriodo}_Despesas_Empenho.csv"
echo "OK"

# Concatena os arquivos de despesas de pagamento
echo -n "Concatenando os arquivos de Despesas Pagamento..."
tail -q -n +2 "$tmpDir"/*_Despesas_Pagamento.csv > "$dataDir/${ano}${mes}${inicioPeriodo}-${fimPeriodo}_Despesas_Pagamento.csv"
echo "OK"

cat $tmpDir/*_Empenho.csv > $dataDir/$ano$mes$inicioPeriodo-$fimPeriodo'_Despesas_Empenho.csv'
cat $tmpDir/*_Pagamento.csv > $dataDir/$ano$mes$inicioPeriodo-$fimPeriodo'_Despesas_Pagamento.csv'

# Diretório temporário é apagado
rm -f $tmpDir/*.csv


