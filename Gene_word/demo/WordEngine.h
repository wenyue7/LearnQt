//****************************************************************
//��Ҫ��.pro�ļ���������
//QT += axcontainer
//****************************************************************
#pragma once
#include <QObject>
#include <QAxObject>
#include <QtCore>

enum lineFormat
{
	LEFT,
	RIGHT,
	MIDDLE,
};

enum tableFormat
{
	FIXATION = 0,
	BASED_ON_CONTENT = 1,
	BASED_ON_WINDOW = 2,
};

class WordEngine : public QObject
{
	Q_OBJECT
public:
	WordEngine();
	~WordEngine();

#pragma region �ļ�����

	//****************************************************************
	//FunctionName : newFile �½�word�ĵ�
	//Param : bool visible �Ƿ���ʾ�ĵ�(true ��ʾword�ĵ���false ����ʾword�ĵ�)
	//****************************************************************
	bool newFile(bool visible = false);

	//****************************************************************
	//FunctionName : save ����word�ĵ�
	//Param : QString savePath �ļ�����Ŀ¼
	//****************************************************************
	bool save(QString savePath);

	//****************************************************************
	//FunctionName : close �ر�word�ĵ����ر�ǰһ��Ҫ���棩
	//****************************************************************
	void close();

#pragma endregion �ļ�����

#pragma region ��ʽ����

	//****************************************************************
	//FunctionName : setLineFormat ���ö��뷽ʽ
	//Param : lineFormat type ���뷽ʽ��LEFT ����룬RIGHT �Ҷ��룬MIDDLE ���У�
	//****************************************************************
	bool setLineFormat(lineFormat type);

	//****************************************************************
	//FunctionName : addEnter ����
	//****************************************************************
	bool addEnter();

	//****************************************************************
	//FunctionName : moveDownSelection ʹ������������Ϊ���Ԫ����ַ�������Ҫʹ�ô˷���ʹ����������
	//****************************************************************
	bool moveDownSelection();

#pragma endregion ��ʽ����

#pragma region �ı���ͼƬ

	//****************************************************************
	//FunctionName : addText ����ı�
	//Param : QString text �ı�
	//****************************************************************
	bool addText(QString text);

	//****************************************************************
	//FunctionName : setFontSize ���������С����Ҫ������ı�ǰ���ã�
	//Param : int fontSize �����С
	//****************************************************************
	bool setFontSize(int fontSize);	

	//****************************************************************
	//FunctionName : setFontName �������壨��Ҫ������ı�ǰ���ã�
	//Param : QString& fontName ������
	//****************************************************************
	bool setFontName(QString& fontName);

	//****************************************************************
	//FunctionName : setFontName ��������Ӵ֣���Ҫ������ı�ǰ���ã�
	//Param : bool flag �Ƿ�Ӵ֣�true �Ӵ֣�false ���Ӵ֣�
	//****************************************************************
	bool setFontBold(bool flag);

	//****************************************************************
	//FunctionName : addPicture ���ͼƬ
	//Param : QString& filePath ͼƬĿ¼
	//****************************************************************
	bool addPicture(QString& filePath);

#pragma endregion �ı���ͼƬ

#pragma region ���
	
	//****************************************************************
	//FunctionName : addPicture ��ӱ��
	//Param : int row ����
	//Param : int column ����
	//Param : tableFormat type ������ɷ�ʽ��FIXATION �̶���С��BASED_ON_CONTENT �������ֵ�����С��BASED_ON_WINDOW ���ݴ��ڵ�����С��
	//****************************************************************
	QAxObject *addTable(int row, int column, tableFormat type);

	//****************************************************************
	//FunctionName : setTableCellString Ϊ���Ԫ����ַ���
	//Param : QAxObject *table ������ָ��
	//Param : int row �кţ���1��ʼ��
	//Param : int column �кţ���1��ʼ��
	//Param : QString text �ַ�������
	//****************************************************************
	bool setTableCellString(QAxObject *table, int row, int column, QString text);

	//****************************************************************
	//FunctionName : setTableCellFontBold ���ñ��Ԫ����Ӵ�
	//Param : QAxObject *table ������ָ��
	//Param : int row �кţ���1��ʼ��
	//Param : int column �кţ���1��ʼ��
	//Param : bool isBold  �Ƿ�Ӵ֣�true �Ӵ֣�false ���Ӵ֣�
	//****************************************************************
	bool setTableCellFontBold(QAxObject *table, int row, int column, bool isBold);

	//****************************************************************
	//FunctionName : setTableCellFontBold ���ñ��Ԫ�����С
	//Param : QAxObject *table ������ָ��
	//Param : int row �кţ���1��ʼ��
	//Param : int column �кţ���1��ʼ��
	//Param : int size  �����С
	//****************************************************************
	bool setTableCellFontSize(QAxObject *table, int row, int column, int size);

	//****************************************************************
	//FunctionName : setTableCellFontName ���ñ��Ԫ����
	//Param : QAxObject *table ������ָ��
	//Param : int row �кţ���1��ʼ��
	//Param : int column �кţ���1��ʼ��
	//Param : QString& fontName ������
	//****************************************************************
	bool setTableCellFontName(QAxObject *table, int row, int column, QString& fontName);

	//****************************************************************
	//FunctionName : setTableCellFontName ���ñ���п�
	//Param : QAxObject *table ������ָ��
	//Param : int column �кţ���1��ʼ��
	//Param : int width ���
	//****************************************************************
	bool setTableColumnWidth(QAxObject *table, int column, int width);

	//****************************************************************
	//FunctionName : setTableCellFontName ���ñ�����и�
	//Param : QAxObject *table ������ָ��
	//Param : int row �кţ���1��ʼ��
	//Param : int height �߶�
	//****************************************************************
	bool setTableColumnHeight(QAxObject *table, int row, int height);

	//****************************************************************
	//FunctionName : setTableCellFontName �ϲ����Ԫ��
	//Param : QAxObject *table ������ָ��
	//Param : int startRow ��ʼ�кţ���1��ʼ��
	//Param : int startColumn ��ʼ�кţ���1��ʼ��
	//Param : int endRow ��ֹ�кţ���1��ʼ��
	//Param : int endColumn ��ֹ�кţ���1��ʼ��
	//****************************************************************
	void mergeTableCells(QAxObject *table, int startRow, int startColumn, int endRow, int endColumn);

#pragma endregion ���

private:
	QAxObject *m_pWord;
	QAxObject *m_pWorkDocument;
	bool m_bIsOpen;
	bool m_bNewFile;
};


