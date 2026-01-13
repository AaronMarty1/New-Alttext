################################################################################
# Copyright (c) 2025 PDFix (http://pdfix.net). All Rights Reserved.
# This file was generated automatically
################################################################################
from ctypes import Structure, c_int, c_bool, c_void_p, c_double, c_float, byref, POINTER, c_wchar_p, c_char_p, c_ubyte, create_unicode_buffer, cdll

# Enumerators
# PdfAuthPlatform
(kAuthPlatformWin, kAuthPlatformMac, kAuthPlatformLinux, kAuthPlatformAndroid, kAuthPlatformiOS, kAuthPlatformServer) = (0, 1, 2, 3, 4, 5)
# PdfAuthOption
(kAuthOptionBasic, kAuthOptionProfessional, kAuthOptionEnterprise, kAuthOptionDeveloper, kAuthOptionTrial, kAuthOptionLite) = (0, 1, 2, 3, 4, 5)
# PdfEventType
(kEventUnknown, kEventDocWillSave, kEventDocWillClose, kEventDocDidOpen, kEventDocDidSave, kEventDocWillChangePages, kEventDocDidChangePages, kEventDocWillDeletePages, kEventDocDidDeletePages, kEventDocWillInsertPages, kEventDocDidInsertPages, kEventDocWillMovePages, kEventDocDidMovePages, kEventDocWillReplacePages, kEventDocDidReplacePages, kEventDocWillChangeFlags, kEventDocDidChangeFlags, kEventAnnotWillChange, kEventAnnotDidChange, kEventPageWillAddAnnot, kEventPageWillRemoveAnnot, kEventPageDidAddAnnot, kEventPageDidRemoveAnnot, kEventPageContentWillChange, kEventPageContentDidChange, kEventPageContentWillWrite, kEventPageContentDidWrite, kEventFormFieldWillChange, kEventFormFieldDidChange, kEventProgressDidChange, kEventBookmarkWillChange, kEventBookmarkDidChange, kEventBookmarkWillRemove, kEventBookmarkDidRemove, kEventBookmarkDidCreate, kEventBookmarkDidChangePosition, kEventUndoDidCreate, kEventUndoWillExecute, kEventUndoDidExecute, kEventUndoWillDestroy, kEventPageMapWillChange, kEventPageMapDidChange, kEventStructTreeWillCreate, kEventStructTreeDidCreate, kEventStructTreeWillRemove, kEventStructTreeDidRemove, kEventStructElementWillAdd, kEventStructElementDidAdd, kEventStructElementWillChange, kEventStructElementDidChange, kEventStructElementChildWillRemove, kEventStructElementChildDidRemove, kEventDocTemplateWillChange, kEventDocTemplateDidChange, kEventObjectWillChange, kEventObjectDidChange, kEventObjectWillDestroy, kEventDidCreate, kEventWillDestroy, kEventWillChange, kEventDidChange, kEventWillWrite, kEventDidWrite) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62)
# 
(kSaveIncremental, kSaveFull, kSaveUncompressed, kSaveCompressedStructureOnly, kSaveIncludeComments) = (0x00, 0x01, 0x02, 0x04, 0x0100)
# 
(kDocNeedsSave, kDocNeedsFullSave, kDocIsModified, kDocIsClosing) = (0x01, 0x03, 0x04, 0x08)
# 
(kPageContentIsModified) = (0x01)
# PdfDigSigValidState
(kDigSigBlank, kDigSigUnknown, kDigSigInvalid, kDigSigValid, kDigSigDoubleChecked, kDigSigValidStateEnumSize) = (0, 1, 2, 3, 4, 5)
# PdfAlignment
(kAlignmentNone, kAlignmentLeft, kAlignmentRight, kAlignmentJustify, kAlignmentTop, kAlignmentBottom, kAlignmentCenter) = (0, 1, 2, 3, 4, 5, 6)
# PdfRotate
(kRotate0, kRotate90, kRotate180, kRotate270) = (0, 90, 180, 270)
# PdfObjectType
(kPdsUnknown, kPdsBoolean, kPdsNumber, kPdsString, kPdsName, kPdsArray, kPdsDictionary, kPdsStream, kPdsNull, kPdsReference) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# PdfPageObjectType
(kPdsPageUnknown, kPdsPageText, kPdsPagePath, kPdsPageImage, kPdsPageShading, kPdsPageForm) = (0, 1, 2, 3, 4, 5)
# PdfElementType
(kPdeUnknown, kPdeText, kPdeTextLine, kPdeWord, kPdeTextRun, kPdeImage, kPdeContainer, kPdeList, kPdeLine, kPdeRect, kPdeTable, kPdeCell, kPdeToc, kPdeFormField, kPdeHeader, kPdeFooter, kPdeArtifact, kPdeAnnot) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
# PdfContainerType
(kPdeContainerUnknown, kPdeContainerPage, kPdeContainerCol, kPdeContainerRow, kPdeContainerSplitter) = (0, 1, 2, 3, 4)
# PdfTagType
(kTagUnknown, kTagSect, kTagArt) = (0, 1, 2)
# PdfLineCap
(kPdfLineCapButt, kPdfLineCapRound, kPdfLineCapSquare) = (0, 1, 2)
# PdfLineJoin
(kPdfLineJoinMiter, kPdfLineJoinRound, kPdfLineJoinBevel) = (0, 1, 2)
# PdfFillType
(kFillTypeNone, kFillTypeSolid, kFillTypePattern) = (0, 1, 2)
# PdfTextAlignment
(kTextAlignmentNone, kTextAlignmentLeft, kTextAlignmentRight, kTextAlignmentCenter, kTextAlignmentJustify) = (0, 1, 2, 3, 4)
# PdfAnnotSubtype
(kAnnotUnknown, kAnnotText, kAnnotLink, kAnnotFreeText, kAnnotLine, kAnnotSquare, kAnnotCircle, kAnnotPolygon, kAnnotPolyLine, kAnnotHighlight, kAnnotUnderline, kAnnotSquiggly, kAnnotStrikeOut, kAnnotStamp, kAnnotCaret, kAnnotInk, kAnnotPopup, kAnnotFileAttachment, kAnnotSound, kAnnotMovie, kAnnotWidget, kAnnotScreen, kAnnotPrinterMark, kAnnotTrapNet, kAnnotWatermark, kAnnot3D, kAnnotRedact) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
# 
(kAnnotFlagNone, kAnnotFlagInvisible, kAnnotFlagHidden, kAnnotFlagPrint, kAnnotFlagNoZoom, kAnnotFlagNoRotate, kAnnotFlagNoView, kAnnotFlagReadOnly, kAnnotFlagLocked, kAnnotFlagToggleNoView, kAnnotFlagLockedContents) = (0x0000, 0x0001, 0x0002, 0x0004, 0x0008, 0x0010, 0x0020, 0x0040, 0x0080, 0x0100, 0x0200)
# 
(kRemoveAnnotSingle, kRemoveAnnotPopup, kRemoveAnnotReply) = (0x0000, 0x0001, 0x0002)
# PdfBorderStyle
(kBorderSolid, kBorderDashed, kBorderBeveled, kBorderInset, kBorderUnderline) = (0, 1, 2, 3, 4)
# 
(kTextFlagNone, kTextFlagUnderline, kTextFlagStrikeout, kTextFlagHighlight, kTextFlagSubscript, kTextFlagSuperscript, kTextFlagNoUnicode, kTextFlagPatternFill, kTextFlagPatternStroke, kTextFlagWhiteSpace, kTextFlagUnicode) = (0x000, 0x001, 0x002, 0x004, 0x008, 0x010, 0x020, 0x040, 0x080, 0x100, 0x200)
# 
(kFieldFlagNone, kFieldFlagReadOnly, kFieldFlagRequired, kFieldFlagNoExport, kFieldFlagMultiline, kFieldFlagPassword, kFieldFlagNoToggleToOff, kFieldFlagRadio, kFieldFlagPushButton, kFieldFlagCombo, kFieldFlagEdit, kFieldFlagSort, kFieldFlagMultiSelect, kFieldFlagDoNotSpellCheck, kFieldFlagDCommitOnSelChange, kFieldFlagFileSelect, kFieldFlagDoNotScroll, kFieldFlagComb, kFieldFlagRichText, kFieldFlagRadiosInUnison) = (0x00000000, 0x00000001, 0x00000002, 0x00000004, 0x00001000, 0x00002000, 0x00004000, 0x00008000, 0x00010000, 0x00200000, 0x00400000, 0x00800000, 0x00200000, 0x00400000, 0x04000000, 0x00100000, 0x00800000, 0x01000000, 0x02000000, 0x02000000)
# PdfFieldType
(kFieldUnknown, kFieldButton, kFieldRadio, kFieldCheck, kFieldText, kFieldCombo, kFieldList, kFieldSignature) = (0, 1, 2, 3, 4, 5, 6, 7)
# PdfActionEventType
(kActionEventAnnotEnter, kActionEventAnnotExit, kActionEventAnnotMouseDown, kActionEventAnnotMouseUp, kActionEventAnnotFocus, kActionEventAnnotBlur, kActionEventAnnotPageOpen, kActionEventAnnotPageClose, kActionEventAnnotPageVisible, kActionEventAnnotPageInvisible, kActionEventPageOpen, kActionEventPageClose, kActionEventFieldKeystroke, kActionEventFieldFormat, kActionEventFieldValidate, kActionEventFieldCalculate, kActionEventDocWillClose, kActionEventDocWillSave, kActionEventDocDidSave, kActionEventDocWillPrint, kActionEventDocDidPrint, kActionEventDocOpen) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)
# PdfActionType
(kActionUnknown, kActionGoTo, kActionGoToR, kActionGoToE, kActionLaunch, kActionThread, kActionURI, kActionSound, kActionMovie, kActionHide, kActionNamed, kActionSubmitForm, kActionResetForm, kActionImportData, kActionJavaScript, kActionSetOCGState, kActionRendition, kActionTrans, kActionGoTo3DView) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
# 
(kRenderAnnot, kRenderLCDText, kRenderNoNativeText, kRenderGrayscale, kRenderLimitedCache, kRenderForceHalftone, kRenderPrinting, kRenderNoText, kRenderNoBackground, kRenderBorder) = (0x001, 0x002, 0x004, 0x008, 0x010, 0x020, 0x040, 0x080, 0x100, 0x200)
# PdfImageFormat
(kImageFormatUnknown, kImageFormatPng, kImageFormatJpg, kImageFormatBmp, kImageFormatEmf, kImageFormatTiff) = (0, 1, 2, 3, 4, 5)
# 
(kFontFixedPitch, kFontSerif, kFontSymbolic, kFontScript, kFontNotSymbolic, kFontItalic, kFontAllCap, kFontSmallCap, kFontForceBold) = (0x00001, 0x00002, 0x00004, 0x00008, 0x00020, 0x00040, 0x10000, 0x20000, 0x40000)
# 
(kContentImage, kContentText, kContentPath, kContentForm, kContentShading, kContentTextTransparent, kContentTextFill, kContentTextStroke) = (0x00001, 0x00002, 0x00004, 0x00008, 0x00020, 0x00040, 0x00080, 0x00100)
# PdfFontCharset
(kFontAnsiCharset, kFontDefaultCharset, kFontSymbolCharset, kFontUnknownCharset, kFontMacintoshCharset, kFontShiftJISCharset, kFontHangeulCharset, kFontKoreanCharset, kFontGB2312Charset, kFontCHineseBig5Charset, kFontGreekCharset, kFontTurkishCharset, kFontVietnameseCharset, kFontHebrewCharset, kFontArabicCharset, kFontArabicTCharset, kFontArabicUCharset, kFontHebrewUCharset, kFontBalticCharset, kFontRussianCharset, kFontThaiCharset, kFontEastEuropeCharset) = (0, 1, 2, 3, 77, 128, 129, 130, 134, 136, 161, 162, 163, 177, 178, 179, 180, 181, 186, 204, 222, 238)
# PdfFontCodepage
(kFontDefANSICodepage, kFontSymbolCodepage, kFontMSDOSUSCodepage, kFontArabicASMO708Codepage, kFontMSDOSGreek1Codepage, kFontMSDOSBalticCodepage, kFontMSDOSWesternEuropeanCodepage, kFontMSDOSEasternEuropeanCodepage, kFontMSDOSCyrillicCodepage, kFontMSDOSTurkishCodepage, kFontMSDOSPortugueseCodepage, kFontMSDOSIcelandicCodepage, kFontMSDOSHebrewCodepage, kFontMSDOSFrenchCanadianCodepage, kFontMSDOSArabicCodepage, kFontMSDOSNorwegianCodepage, kFontMSDOSRussianCodepage, kFontMSDOSGreek2Codepage, kFontMSDOSThaiCodepage, kFontShiftJISCodepage, kFontChineseSimplifiedCodepage, kFontHangulCodepage, kFontChineseTraditionalCodepage, kFontUTF16LECodepage, kFontUTF16BECodepage, kFontMSWinEasternEuropeanCodepage, kFontMSWinCyrillicCodepage, kFontMSWinWesternEuropeanCodepage, kFontMSWinGreekCodepage, kFontMSWinTurkishCodepage, kFontMSWinHebrewCodepage, kFontMSWinArabicCodepage, kFontMSWinBalticCodepage, kFontMSWinVietnameseCodepage, kFontJohabCodepage, kFontMACRomanCodepage, kFontMACShiftJISCodepage, kFontMACChineseTraditionalCodepage, kFontMACKoreanCodepage, kFontMACArabicCodepage, kFontMACHebrewCodepage, kFontMACGreekCodepage, kFontMACCyrillicCodepage, kFontMACChineseSimplifiedCodepage, kFontMACThaiCodepage, kFontMACEasternEuropeanCodepage, kFontMACTurkishCodepage, kFontUTF8Codepage) = (0, 42, 437, 708, 737, 775, 850, 852, 855, 857, 860, 861, 862, 863, 864, 865, 866, 869, 874, 932, 936, 949, 950, 1200, 1201, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1361, 10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10021, 10029, 10081, 65001)
# 
(kFontCreateNormal, kFontCreateEmbedded, kFontCreateSubset, kFontCreateDoNotEmbed, kFontCreateEncodeByGID, kFontCreateDeferWidths, kFontCreateGIDOverride, kFontCreateToUnicode, kFontCreateAllWidths, kFontCreateEmbedOpenType) = (0, 0x0001, 0x0002, 0x0004, 0x0008, 0x0010, 0x0020, 0x0040, 0x0080, 0x0100)
# PdfFontType
(kFontUnknownType, kFontType1, kFontTrueType, kFontType3, kFontCIDFont) = (0, 1, 2, 3, 4)
# PdfFontFormat
(kFontFormatTtf, kFontFormatWoff) = (0, 1)
# PdfDestZoomType
(kPdfZoomXYZ, kPdfZoomFitPage, kPdfZoomFitHorz, kPdfZoomFitVert, kPdfZoomFitRect, kPdfZoomFitBbox, kPdfZoomFitBHorz, kPdfZoomFitBVert) = (1, 2, 3, 4, 5, 6, 7, 8)
# PdfDigSigType
(kDigSigOpenSSL, kDigSigCert, kDigSigCustom) = (0, 1, 2)
# PdfImageType
(kImageFigure, kImageImage, kImagePath, kImageRect, kImageShading, kImageForm) = (0, 1, 2, 3, 4, 5)
# 
(kTableUnknown, kTableGraphic, kTableIsolated, kTableIsolatedCol, kTableIsolatedRow, kTableForm, kTableElement, kTableToc) = (0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40)
# PdfListType
(kListNone, kListUnordered, kListOrdered, kListDisc, kListCircle, kListSquare, kListDecimal, kListRomanUpper, kListRomanLower, kListLetterUpper, kListLetterLower, kListDescription) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# 
(kWordFlagHyphen, kWordFlagBullet, kWordFlagColon, kWordFlagNumber, kWordFlagSubscript, kWordFlagSupercript, kWordFlagTerminal, kWordFlagFirstCap, kWordFlagImage, kWordFlagNumberingDecimal, kWordFlagNumberingRoman, kWordFlagNumberingLetter, kWordFlagPageNumber, kWordFlagFilling, kWordFlagAllCaps, kWordFlagComma, kWordFlagNoUnicode, kWordFlagLabel, kWordFlagLabelLetter, kWordFlagLabelNum, kWordFlagLabelRomanNum, kWordFlagCurrency, kWordFlagMathSymbol) = (0x0001, 0x0002, 0x0004, 0x008, 0x0010, 0x0020, 0x0040, 0x0080, 0x00100, 0x0200, 0x0400, 0x0800, 0x1000, 0x2000, 0x4000, 0x8000, 0x10000, 0x20000, 0x40000, 0x080000, 0x100000, 0x200000, 0x400000)
# 
(kTextLineFlagHyphen, kTextLineFlagNewLine, kTextLineFlagIndent, kTextLineFlagTerminal, kTextLineFlagDropCap, kTextLineFlagFilling, kTextLineFlagAllCaps, kTextLineFlagNoNewLine) = (0x0001, 0x0002, 0x0004, 0x0008, 0x0010, 0x0020, 0x0040, 0x0080)
# PdfTextStyle
(kTextNormal, kTextH1, kTextH2, kTextH3, kTextH4, kTextH5, kTextH6, kTextH7, kTextH8, kTextNote, kTextTitle) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# 
(kTextFlagTableCaption, kTextFlagImageCaption, kTextFlagChartCaption, kTextFlagNoteCaption, kTextFlagFilling, kTextFlagAllCaps, kTextFlagNewLine, kTextFlagNoNewLine) = (0x0001, 0x0002, 0x0004, 0x0008, 0x010, 0x020, 0x040, 0x080)
# 
(kCellScopeNone, kCellScopeRow, kCellScopeCol) = (0x00, 0x01, 0x02)
# 
(kTableErrorNone, kTableErrorNoRow, kTableErrorRowSpan, kTableErrorColSpan) = (0x00, 0x01, 0x02, 0x04)
# 
(kElemNoJoin, kElemNoSplit, kElemArtifact, kElemHeader, kElemFooter, kElemSplitter, kElemNoTable, kElemNoImage, kElemInitial, kElemNoExpand, kElemContinuous, kElemAnchor) = (0x001, 0x002, 0x004, 0x008, 0x010, 0x020, 0x040, 0x080, 0x100, 0x200, 0x400, 0x800)
# PsFileMode
(kPsWrite, kPsReadOnly, kPsTruncate) = (0, 1, 2)
# PdfAlternateType
(kAlternatePdf, kAlternateHtml) = (0, 1)
# PdfMediaType
(kCSSMediaTypeAll, kCSSMediaTypePrint, kCSSMediaTypeScreen, kCSSMediaTypeSpeech) = (0, 1, 2, 3)
# PsImageDIBFormat
(kImageDIBFormatRgb32, kImageDIBFormatArgb) = (0x020, 0x220)
# PsDataFormat
(kDataFormatJson, kDataFormatXml, kDataFormatTxt) = (0, 1, 2)
# PsRenderDeviceType
(kRenderDeviceTypeGDI, kRenderDeviceTypeDirectX) = (0, 1)
# PdfStreamType
(kFileStream, kMemoryStream, kProcStream) = (0, 1, 2)
# PdfStructElementType
(kPdsStructChildInvalid, kPdsStructChildElement, kPdsStructChildPageContent, kPdsStructChildStreamContent, kPdsStructChildObject) = (0, 1, 2, 3, 4)
# 
(kPageInsertNone, kPageInsertBookmarks, kPageInsertAll) = (0x0000, 0x001, 0x0002)
# PdfAuthorizationType
(kAuthorizationStandard, kAuthorizationAccount) = (0, 1)
# PdfDestFitType
(kDestFitUnknown, kDestFitXYZ, kDestFit, kDestFitH, kDestFitV, kDestFitR, kDestFitB, kDestFitBH, kDestFitBV) = (0, 1, 2, 3, 4, 5, 6, 7, 8)
# PdfLabelType
(kLabelNo, kLabelNone, kLabel, kLabelLevel1, kLabelLevel2, kLabelLevel3, kLabelLevel4) = (-1, 0, 1, 2, 3, 4, 5)
# PdfAnnotAppearanceMode
(kAppearanceNormal, kAppearanceRollover, kAppearanceDown) = (0, 1, 2)
# PdsPathPointType
(kPathLineTo, kPathBezierTo, kPathMoveTo) = (0, 1, 2)
# PdfBlendMode
(kBlendModeNormal, kBlendModeMultiply, kBlendModeScreen, kBlendModeOverlay, kBlendModeDarken, kBlendModeLighten, kBlendModeColorDodge, kBlendModeColorBurn, kBlendModeHardLight, kBlendModeSoftLight, kBlendModeDifference, kBlendModeExclusion, kBlendModeHue, kBlendModeSaturation, kBlendModeColor, kBlendModeLuminosity) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 22, 23, 24)
# PdfFillRule
(kFillRuleNone, kFillRuleEvenOdd, kFillRuleWinding) = (0, 1, 2)
# 
(kContentToPage, kContentToForm, kContentToCharproc) = (0x01, 0x02, 0x04)
# PdfColorSpaceFamily
(kColorSpaceUnknown, kColorSpaceDeviceGray, kColorSpaceDeviceRGB, kColorSpaceDeviceCMYK, kColorSpaceCalGray, kColorSpaceCalRGB, kColorSpaceLab, kColorSpaceICCBase, kColorSpaceSeparation, kColorSpaceDeviceN, kColorSpaceIndexed, kColorSpacePattern) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# 
(kStateDefault, kStateNoRender, kStateExclude) = (0, 0x01, 0x02)
# 
(kInsertBeforeFirst, kInsertAfterLast) = (0, -1)
# PdfWordFinderAlgorithm
(kWordFinderAlgLatest, kWordFinderAlgBasic) = (-1, 0)
# 
(kWordFinderDefault, kWordFinderStateFlags) = (0, 0x01)
# 
(kUserPermissionNone, kUserPermissionAll, kUserPermissionMask, kUserPermissionPrint, kUserPermissionModify, kUserPermissionExtract, kUserPermissionModifyAnnots, kUserPermissionFillForms, kUserPermissionExtractAccessibility, kUserPermissionAssembleDoc, kUserPermissionPrintHighRes) = (0, -1, 0x0F3C, 0x0004, 0x0008, 0x0010, 0x0020, 0x0100, 0x0200, 0x0400, 0x0800)
# PdfPermissionLevel
(kPermissionLevelUser, kPermissionLevelOwner) = (0, 1)
# PdfStandardEncryptionMethod
(kStandardEncryptionMethodNone, kStandardEncryptionMethodRC4v2, kStandardEncryptionMethodAESv1, kStandardEncryptionMethodAESv2) = (0, 1, 2, 3)
# 
(kContentMarkMcid, kContentMarkArtifact, kContentMarkCustom) = (0x01, 0x02, 0x04)
# 
(kPdfStandardNone, kPdfStandardPdfA, kPdfStandardPdfUA, kPdfStandardPdfX, kPdfStandardPdfE, kPdfStandardPdfVT) = (0, 0x0001, 0x0002, 0x0004, 0x0008, 0x0010)
# 
(kHtmlNone, kHtmlExportJavaScripts, kHtmlExportFonts, kHtmlRetainFontSize, kHtmlRetainTextColor, kHtml41Support, kHtmlNoExternalCSS, kHtmlNoExternalJS, kHtmlNoExternalIMG, kHtmlNoExternalFONT, kHtmlGrayBackground, kHtmlNoPageRender, kHtmlNoHeadNode, kHtmlNoDocumentNode, kHtmlNoPagesNode) = (0x0000, 0x0001, 0x0002, 0x0004, 0x0008, 0x0010, 0x0020, 0x0040, 0x0080, 0x0100, 0x0200, 0x0400, 0x0800, 0x1000, 0x2000)
# 
(kJsonNone, kJsonExportDocInfo, kJsonExportPageInfo, kJsonExportPageContent, kJsonExportStructTree, kJsonExportPageMap, kJsonExportBBox, kJsonExportContentMarks, kJsonExportText, kJsonExportTextStyle, kJsonExportTextState, kJsonExportImages, kJsonExportAnnotations, kJsonExportBookmarks) = (0x00000000, 0x00000001, 0x00000002, 0x00000010, 0x00000020, 0x00000040, 0x00000100, 0x00000200, 0x00001000, 0x00002000, 0x00004000, 0x00010000, 0x00020000, 0x00040000)
# PdfHtmlType
(kPdfHtmlFixed, kPdfHtmlResponsive, kPdfHtmlDerivation) = (0, 1, 2)
# PdfEnumResultType
(kEnumResultError, kEnumResultOk, kEnumResultContinue, kEnumResultContinueSkip) = (0, 1, 2, 3)
# PdfSelectionType
(kPdfSelectionUnknown, kPdfSelectionPageObject, kPdfSelectionPage, kPdfSelectionStructElement, kPdfSelectionAnnot, kPdfSelectionFont) = (0, 1, 2, 3, 4, 5)
# 
(kEnumNone, kEnumReverseOrder, kEnumChildrenFirst, kEnumForms, kEnumFormsProc, kEnumChars) = (0x00, 0x01, 0x02, 0x04, 0x08, 0x10)
# PsCommandType
(kActionBase, kActionMakeAccessible, kActionAutofix, kActionQuickfix, kActionLast) = (0, 1, 2, 3, 4)
# 
(kTextNone, kTextRtl) = (0x01, 0x02)

# Structures - Private
class zz_PdfPoint(Structure):
    _fields_ = [("x", c_float), ("y", c_float)]

class zz_PdfDevPoint(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]

class zz_PdfRect(Structure):
    _fields_ = [("left", c_float), ("top", c_float), ("right", c_float), ("bottom", c_float)]

class zz_PdfDevRect(Structure):
    _fields_ = [("left", c_int), ("top", c_int), ("right", c_int), ("bottom", c_int)]

class zz_PdfQuad(Structure):
    _fields_ = [("tl", zz_PdfPoint), ("tr", zz_PdfPoint), ("bl", zz_PdfPoint), ("br", zz_PdfPoint)]

class zz_PdfDevQuad(Structure):
    _fields_ = [("tl", zz_PdfDevPoint), ("tr", zz_PdfDevPoint), ("bl", zz_PdfDevPoint), ("br", zz_PdfDevPoint)]

class zz_PdfMatrix(Structure):
    _fields_ = [("a", c_float), ("b", c_float), ("c", c_float), ("d", c_float), ("e", c_float), ("f", c_float)]

class zz_PdfGray(Structure):
    _fields_ = [("gray", c_int)]

class zz_PdfRGB(Structure):
    _fields_ = [("r", c_int), ("g", c_int), ("b", c_int)]

class zz_PdfCMYK(Structure):
    _fields_ = [("c", c_int), ("m", c_int), ("y", c_int), ("k", c_int)]

class zz_PdfColorState(Structure):
    _fields_ = [("fill_type", c_int), ("stroke_type", c_int), ("fill_color", c_void_p), ("stroke_color", c_void_p), ("fill_opacity", c_int), ("stroke_opacity", c_int)]

class zz_PdeColorState(Structure):
    _fields_ = [("fill_type", c_int), ("stroke_type", c_int), ("fill_color", zz_PdfRGB), ("stroke_color", zz_PdfRGB), ("fill_opacity", c_int), ("stroke_opacity", c_int)]

class zz_PdfTextState(Structure):
    _fields_ = [("color_state", zz_PdfColorState), ("font", c_void_p), ("font_size", c_float), ("char_spacing", c_float), ("word_spacing", c_float), ("flags", c_int)]

class zz_PdfGraphicState(Structure):
    _fields_ = [("color_state", zz_PdfColorState), ("line_width", c_float), ("miter_limit", c_float), ("line_cap", c_int), ("line_join", c_int), ("blend_mode", c_int), ("matrix", zz_PdfMatrix)]

class zz_PdeGraphicState(Structure):
    _fields_ = [("color_state", zz_PdeColorState), ("line_width", c_float), ("miter_limit", c_float), ("line_cap", c_int), ("line_join", c_int), ("blend_mode", c_int), ("matrix", zz_PdfMatrix)]

class zz_PdfFontState(Structure):
    _fields_ = [("type", c_int), ("flags", c_int), ("bbox", zz_PdfRect), ("ascent", c_int), ("descent", c_int), ("italic", c_int), ("bold", c_int), ("fixed_width", c_int), ("vertical", c_int), ("embedded", c_int), ("height", c_int)]

class zz_PdfPageRenderParams(Structure):
    _fields_ = [("device", c_void_p), ("image", c_void_p), ("matrix", zz_PdfMatrix), ("clip_box", zz_PdfRect), ("render_flags", c_int)]

class zz_PdfTiffParams(Structure):
    _fields_ = [("dpi", c_int), ("render_flags", c_int)]

class zz_PdfAnnotAppearance(Structure):
    _fields_ = [("fill_color", zz_PdfRGB), ("fill_type", c_int), ("border_color", zz_PdfRGB), ("border_width", c_float), ("border", c_int), ("opacity", c_float), ("font_size", c_float), ("text_align", c_int)]

class zz_PdfBookmarkAppearance(Structure):
    _fields_ = [("color", zz_PdfRGB), ("italic", c_int), ("bold", c_int)]

class zz_PdfWhitespaceParams(Structure):
    _fields_ = [("width", c_float), ("height", c_float)]

class zz_PdfMediaQueryParams(Structure):
    _fields_ = [("type", c_int), ("min_width", c_int)]

class zz_PdfImageParams(Structure):
    _fields_ = [("format", c_int), ("quality", c_int)]

class zz_PdfTagsParams(Structure):
    _fields_ = [("standard_attrs", c_int), ("css_attrs", c_int), ("headings", c_int)]

class zz_PdsContentParams(Structure):
    _fields_ = [("flags", c_int), ("form_type", c_int), ("bbox", zz_PdfRect), ("matrix", zz_PdfMatrix)]

class zz_PdfStandardSecurityParams(Structure):
    _fields_ = [("permissions", c_int), ("revision", c_int), ("encrypt_method", c_int), ("encrypt_metadata", c_int)]

class zz_PdfHtmlParams(Structure):
    _fields_ = [("flags", c_int), ("width", c_int), ("type", c_int), ("image_params", zz_PdfImageParams)]

class zz_PdfJsonParams(Structure):
    _fields_ = [("flags", c_int)]

class zz_PsImageInfo(Structure):
    _fields_ = [("width", c_int), ("height", c_int), ("page_count", c_int)]

class zz_PdfCellParams(Structure):
    _fields_ = [("scope", c_int), ("header", c_int), ("row_span", c_int), ("col_span", c_int), ("row", c_int), ("col", c_int)]

# Structures - Public
class PdfPoint(Structure):
    def __init__(self):
        self.x = 0
        self.y = 0
    def GetIntStruct(self):
        result = zz_PdfPoint()
        result.x = self.x
        result.y = self.y
        return result
    def SetIntStruct(self, struct):
        self.x = struct.x
        self.y = struct.y

class PdfDevPoint(Structure):
    def __init__(self):
        self.x = 0
        self.y = 0
    def GetIntStruct(self):
        result = zz_PdfDevPoint()
        result.x = self.x
        result.y = self.y
        return result
    def SetIntStruct(self, struct):
        self.x = struct.x
        self.y = struct.y

class PdfRect(Structure):
    def __init__(self):
        self.left = 0
        self.top = 0
        self.right = 0
        self.bottom = 0
    def GetIntStruct(self):
        result = zz_PdfRect()
        result.left = self.left
        result.top = self.top
        result.right = self.right
        result.bottom = self.bottom
        return result
    def SetIntStruct(self, struct):
        self.left = struct.left
        self.top = struct.top
        self.right = struct.right
        self.bottom = struct.bottom

class PdfDevRect(Structure):
    def __init__(self):
        self.left = 0
        self.top = 0
        self.right = 0
        self.bottom = 0
    def GetIntStruct(self):
        result = zz_PdfDevRect()
        result.left = self.left
        result.top = self.top
        result.right = self.right
        result.bottom = self.bottom
        return result
    def SetIntStruct(self, struct):
        self.left = struct.left
        self.top = struct.top
        self.right = struct.right
        self.bottom = struct.bottom

class PdfQuad(Structure):
    def __init__(self):
        self.tl = PdfPoint()
        self.tr = PdfPoint()
        self.bl = PdfPoint()
        self.br = PdfPoint()
    def GetIntStruct(self):
        result = zz_PdfQuad()
        result.tl = self.tl.GetIntStruct()
        result.tr = self.tr.GetIntStruct()
        result.bl = self.bl.GetIntStruct()
        result.br = self.br.GetIntStruct()
        return result
    def SetIntStruct(self, struct):
        self.tl.SetIntStruct(struct.tl)
        self.tr.SetIntStruct(struct.tr)
        self.bl.SetIntStruct(struct.bl)
        self.br.SetIntStruct(struct.br)

class PdfDevQuad(Structure):
    def __init__(self):
        self.tl = PdfDevPoint()
        self.tr = PdfDevPoint()
        self.bl = PdfDevPoint()
        self.br = PdfDevPoint()
    def GetIntStruct(self):
        result = zz_PdfDevQuad()
        result.tl = self.tl.GetIntStruct()
        result.tr = self.tr.GetIntStruct()
        result.bl = self.bl.GetIntStruct()
        result.br = self.br.GetIntStruct()
        return result
    def SetIntStruct(self, struct):
        self.tl.SetIntStruct(struct.tl)
        self.tr.SetIntStruct(struct.tr)
        self.bl.SetIntStruct(struct.bl)
        self.br.SetIntStruct(struct.br)

class PdfMatrix(Structure):
    def __init__(self):
        self.a = 1
        self.b = 0
        self.c = 0
        self.d = 1
        self.e = 0
        self.f = 0
    def GetIntStruct(self):
        result = zz_PdfMatrix()
        result.a = self.a
        result.b = self.b
        result.c = self.c
        result.d = self.d
        result.e = self.e
        result.f = self.f
        return result
    def SetIntStruct(self, struct):
        self.a = struct.a
        self.b = struct.b
        self.c = struct.c
        self.d = struct.d
        self.e = struct.e
        self.f = struct.f

class PdfGray(Structure):
    def __init__(self):
        self.gray = 0
    def GetIntStruct(self):
        result = zz_PdfGray()
        result.gray = self.gray
        return result
    def SetIntStruct(self, struct):
        self.gray = struct.gray

class PdfRGB(Structure):
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
    def GetIntStruct(self):
        result = zz_PdfRGB()
        result.r = self.r
        result.g = self.g
        result.b = self.b
        return result
    def SetIntStruct(self, struct):
        self.r = struct.r
        self.g = struct.g
        self.b = struct.b

class PdfCMYK(Structure):
    def __init__(self):
        self.c = 0
        self.m = 0
        self.y = 0
        self.k = 0
    def GetIntStruct(self):
        result = zz_PdfCMYK()
        result.c = self.c
        result.m = self.m
        result.y = self.y
        result.k = self.k
        return result
    def SetIntStruct(self, struct):
        self.c = struct.c
        self.m = struct.m
        self.y = struct.y
        self.k = struct.k

class PdfColorState(Structure):
    def __init__(self):
        self.fill_type = kFillTypeNone
        self.stroke_type = kFillTypeNone
        self.fill_color = None
        self.stroke_color = None
        self.fill_opacity = 255
        self.stroke_opacity = 255
    def GetIntStruct(self):
        result = zz_PdfColorState()
        result.fill_type = self.fill_type
        result.stroke_type = self.stroke_type
        result.fill_color = self.fill_color.obj if self.fill_color != None else None
        result.stroke_color = self.stroke_color.obj if self.stroke_color != None else None
        result.fill_opacity = self.fill_opacity
        result.stroke_opacity = self.stroke_opacity
        return result
    def SetIntStruct(self, struct):
        self.fill_type = struct.fill_type
        self.stroke_type = struct.stroke_type
        self.fill_color = PdfColor(struct.fill_color) if struct.fill_color != None else None
        self.stroke_color = PdfColor(struct.stroke_color) if struct.stroke_color != None else None
        self.fill_opacity = struct.fill_opacity
        self.stroke_opacity = struct.stroke_opacity

class PdeColorState(Structure):
    def __init__(self):
        self.fill_type = kFillTypeNone
        self.stroke_type = kFillTypeNone
        self.fill_color = PdfRGB()
        self.stroke_color = PdfRGB()
        self.fill_opacity = 255
        self.stroke_opacity = 255
    def GetIntStruct(self):
        result = zz_PdeColorState()
        result.fill_type = self.fill_type
        result.stroke_type = self.stroke_type
        result.fill_color = self.fill_color.GetIntStruct()
        result.stroke_color = self.stroke_color.GetIntStruct()
        result.fill_opacity = self.fill_opacity
        result.stroke_opacity = self.stroke_opacity
        return result
    def SetIntStruct(self, struct):
        self.fill_type = struct.fill_type
        self.stroke_type = struct.stroke_type
        self.fill_color.SetIntStruct(struct.fill_color)
        self.stroke_color.SetIntStruct(struct.stroke_color)
        self.fill_opacity = struct.fill_opacity
        self.stroke_opacity = struct.stroke_opacity

class PdfTextState(Structure):
    def __init__(self):
        self.color_state = PdfColorState()
        self.font = None
        self.font_size = 0
        self.char_spacing = 0
        self.word_spacing = 0
        self.flags = 0
    def GetIntStruct(self):
        result = zz_PdfTextState()
        result.color_state = self.color_state.GetIntStruct()
        result.font = self.font.obj if self.font != None else None
        result.font_size = self.font_size
        result.char_spacing = self.char_spacing
        result.word_spacing = self.word_spacing
        result.flags = self.flags
        return result
    def SetIntStruct(self, struct):
        self.color_state.SetIntStruct(struct.color_state)
        self.font = PdfFont(struct.font) if struct.font != None else None
        self.font_size = struct.font_size
        self.char_spacing = struct.char_spacing
        self.word_spacing = struct.word_spacing
        self.flags = struct.flags

class PdfGraphicState(Structure):
    def __init__(self):
        self.color_state = PdfColorState()
        self.line_width = 1
        self.miter_limit = 10
        self.line_cap = kPdfLineCapButt
        self.line_join = kPdfLineJoinMiter
        self.blend_mode = kBlendModeNormal
        self.matrix = PdfMatrix()
    def GetIntStruct(self):
        result = zz_PdfGraphicState()
        result.color_state = self.color_state.GetIntStruct()
        result.line_width = self.line_width
        result.miter_limit = self.miter_limit
        result.line_cap = self.line_cap
        result.line_join = self.line_join
        result.blend_mode = self.blend_mode
        result.matrix = self.matrix.GetIntStruct()
        return result
    def SetIntStruct(self, struct):
        self.color_state.SetIntStruct(struct.color_state)
        self.line_width = struct.line_width
        self.miter_limit = struct.miter_limit
        self.line_cap = struct.line_cap
        self.line_join = struct.line_join
        self.blend_mode = struct.blend_mode
        self.matrix.SetIntStruct(struct.matrix)

class PdeGraphicState(Structure):
    def __init__(self):
        self.color_state = PdeColorState()
        self.line_width = 1
        self.miter_limit = 10
        self.line_cap = kPdfLineCapButt
        self.line_join = kPdfLineJoinMiter
        self.blend_mode = kBlendModeNormal
        self.matrix = PdfMatrix()
    def GetIntStruct(self):
        result = zz_PdeGraphicState()
        result.color_state = self.color_state.GetIntStruct()
        result.line_width = self.line_width
        result.miter_limit = self.miter_limit
        result.line_cap = self.line_cap
        result.line_join = self.line_join
        result.blend_mode = self.blend_mode
        result.matrix = self.matrix.GetIntStruct()
        return result
    def SetIntStruct(self, struct):
        self.color_state.SetIntStruct(struct.color_state)
        self.line_width = struct.line_width
        self.miter_limit = struct.miter_limit
        self.line_cap = struct.line_cap
        self.line_join = struct.line_join
        self.blend_mode = struct.blend_mode
        self.matrix.SetIntStruct(struct.matrix)

class PdfFontState(Structure):
    def __init__(self):
        self.type = kFontUnknownType
        self.flags = 0
        self.bbox = PdfRect()
        self.ascent = 0
        self.descent = 0
        self.italic = 0
        self.bold = 0
        self.fixed_width = 0
        self.vertical = 0
        self.embedded = 0
        self.height = 0
    def GetIntStruct(self):
        result = zz_PdfFontState()
        result.type = self.type
        result.flags = self.flags
        result.bbox = self.bbox.GetIntStruct()
        result.ascent = self.ascent
        result.descent = self.descent
        result.italic = self.italic
        result.bold = self.bold
        result.fixed_width = self.fixed_width
        result.vertical = self.vertical
        result.embedded = self.embedded
        result.height = self.height
        return result
    def SetIntStruct(self, struct):
        self.type = struct.type
        self.flags = struct.flags
        self.bbox.SetIntStruct(struct.bbox)
        self.ascent = struct.ascent
        self.descent = struct.descent
        self.italic = struct.italic
        self.bold = struct.bold
        self.fixed_width = struct.fixed_width
        self.vertical = struct.vertical
        self.embedded = struct.embedded
        self.height = struct.height

class PdfPageRenderParams(Structure):
    def __init__(self):
        self.device = None
        self.image = None
        self.matrix = PdfMatrix()
        self.clip_box = PdfRect()
        self.render_flags = kRenderAnnot
    def GetIntStruct(self):
        result = zz_PdfPageRenderParams()
        result.device = self.device.obj if self.device != None else None
        result.image = self.image.obj if self.image != None else None
        result.matrix = self.matrix.GetIntStruct()
        result.clip_box = self.clip_box.GetIntStruct()
        result.render_flags = self.render_flags
        return result
    def SetIntStruct(self, struct):
        self.device = PsRenderDeviceContext(struct.device) if struct.device != None else None
        self.image = PsImage(struct.image) if struct.image != None else None
        self.matrix.SetIntStruct(struct.matrix)
        self.clip_box.SetIntStruct(struct.clip_box)
        self.render_flags = struct.render_flags

class PdfTiffParams(Structure):
    def __init__(self):
        self.dpi = 72
        self.render_flags = kRenderAnnot
    def GetIntStruct(self):
        result = zz_PdfTiffParams()
        result.dpi = self.dpi
        result.render_flags = self.render_flags
        return result
    def SetIntStruct(self, struct):
        self.dpi = struct.dpi
        self.render_flags = struct.render_flags

class PdfAnnotAppearance(Structure):
    def __init__(self):
        self.fill_color = PdfRGB()
        self.fill_type = kFillTypeNone
        self.border_color = PdfRGB()
        self.border_width = 1
        self.border = kBorderSolid
        self.opacity = 1
        self.font_size = 0
        self.text_align = kTextAlignmentLeft
    def GetIntStruct(self):
        result = zz_PdfAnnotAppearance()
        result.fill_color = self.fill_color.GetIntStruct()
        result.fill_type = self.fill_type
        result.border_color = self.border_color.GetIntStruct()
        result.border_width = self.border_width
        result.border = self.border
        result.opacity = self.opacity
        result.font_size = self.font_size
        result.text_align = self.text_align
        return result
    def SetIntStruct(self, struct):
        self.fill_color.SetIntStruct(struct.fill_color)
        self.fill_type = struct.fill_type
        self.border_color.SetIntStruct(struct.border_color)
        self.border_width = struct.border_width
        self.border = struct.border
        self.opacity = struct.opacity
        self.font_size = struct.font_size
        self.text_align = struct.text_align

class PdfBookmarkAppearance(Structure):
    def __init__(self):
        self.color = PdfRGB()
        self.italic = 0
        self.bold = 0
    def GetIntStruct(self):
        result = zz_PdfBookmarkAppearance()
        result.color = self.color.GetIntStruct()
        result.italic = self.italic
        result.bold = self.bold
        return result
    def SetIntStruct(self, struct):
        self.color.SetIntStruct(struct.color)
        self.italic = struct.italic
        self.bold = struct.bold

class PdfWhitespaceParams(Structure):
    def __init__(self):
        self.width = 0
        self.height = 0
    def GetIntStruct(self):
        result = zz_PdfWhitespaceParams()
        result.width = self.width
        result.height = self.height
        return result
    def SetIntStruct(self, struct):
        self.width = struct.width
        self.height = struct.height

class PdfMediaQueryParams(Structure):
    def __init__(self):
        self.type = kCSSMediaTypeAll
        self.min_width = 1200
    def GetIntStruct(self):
        result = zz_PdfMediaQueryParams()
        result.type = self.type
        result.min_width = self.min_width
        return result
    def SetIntStruct(self, struct):
        self.type = struct.type
        self.min_width = struct.min_width

class PdfImageParams(Structure):
    def __init__(self):
        self.format = kImageFormatPng
        self.quality = 100
    def GetIntStruct(self):
        result = zz_PdfImageParams()
        result.format = self.format
        result.quality = self.quality
        return result
    def SetIntStruct(self, struct):
        self.format = struct.format
        self.quality = struct.quality

class PdfTagsParams(Structure):
    def __init__(self):
        self.standard_attrs = 0
        self.css_attrs = 0
        self.headings = 1
    def GetIntStruct(self):
        result = zz_PdfTagsParams()
        result.standard_attrs = self.standard_attrs
        result.css_attrs = self.css_attrs
        result.headings = self.headings
        return result
    def SetIntStruct(self, struct):
        self.standard_attrs = struct.standard_attrs
        self.css_attrs = struct.css_attrs
        self.headings = struct.headings

class PdsContentParams(Structure):
    def __init__(self):
        self.flags = 0
        self.form_type = 1
        self.bbox = PdfRect()
        self.matrix = PdfMatrix()
    def GetIntStruct(self):
        result = zz_PdsContentParams()
        result.flags = self.flags
        result.form_type = self.form_type
        result.bbox = self.bbox.GetIntStruct()
        result.matrix = self.matrix.GetIntStruct()
        return result
    def SetIntStruct(self, struct):
        self.flags = struct.flags
        self.form_type = struct.form_type
        self.bbox.SetIntStruct(struct.bbox)
        self.matrix.SetIntStruct(struct.matrix)

class PdfStandardSecurityParams(Structure):
    def __init__(self):
        self.permissions = kUserPermissionAll
        self.revision = 4
        self.encrypt_method = kStandardEncryptionMethodAESv1
        self.encrypt_metadata = 0
    def GetIntStruct(self):
        result = zz_PdfStandardSecurityParams()
        result.permissions = self.permissions
        result.revision = self.revision
        result.encrypt_method = self.encrypt_method
        result.encrypt_metadata = self.encrypt_metadata
        return result
    def SetIntStruct(self, struct):
        self.permissions = struct.permissions
        self.revision = struct.revision
        self.encrypt_method = struct.encrypt_method
        self.encrypt_metadata = struct.encrypt_metadata

class PdfHtmlParams(Structure):
    def __init__(self):
        self.flags = 0
        self.width = 1200
        self.type = kPdfHtmlFixed
        self.image_params = PdfImageParams()
    def GetIntStruct(self):
        result = zz_PdfHtmlParams()
        result.flags = self.flags
        result.width = self.width
        result.type = self.type
        result.image_params = self.image_params.GetIntStruct()
        return result
    def SetIntStruct(self, struct):
        self.flags = struct.flags
        self.width = struct.width
        self.type = struct.type
        self.image_params.SetIntStruct(struct.image_params)

class PdfJsonParams(Structure):
    def __init__(self):
        self.flags = kJsonExportDocInfo
    def GetIntStruct(self):
        result = zz_PdfJsonParams()
        result.flags = self.flags
        return result
    def SetIntStruct(self, struct):
        self.flags = struct.flags

class PsImageInfo(Structure):
    def __init__(self):
        self.width = 0
        self.height = 0
        self.page_count = 1
    def GetIntStruct(self):
        result = zz_PsImageInfo()
        result.width = self.width
        result.height = self.height
        result.page_count = self.page_count
        return result
    def SetIntStruct(self, struct):
        self.width = struct.width
        self.height = struct.height
        self.page_count = struct.page_count

class PdfCellParams(Structure):
    def __init__(self):
        self.scope = kCellScopeNone
        self.header = 0
        self.row_span = 1
        self.col_span = 1
        self.row = 0
        self.col = 0
    def GetIntStruct(self):
        result = zz_PdfCellParams()
        result.scope = self.scope
        result.header = self.header
        result.row_span = self.row_span
        result.col_span = self.col_span
        result.row = self.row
        result.col = self.col
        return result
    def SetIntStruct(self, struct):
        self.scope = struct.scope
        self.header = struct.header
        self.row_span = struct.row_span
        self.col_span = struct.col_span
        self.row = struct.row
        self.col = struct.col

# Objects
class _PdfixBase(object):
    def __init__(self, _obj):
        self.obj = _obj

# forward class declaration
class PdsObject: pass
class PdsBoolean: pass
class PdsNumber: pass
class PdsString: pass
class PdsName: pass
class PdsArray: pass
class PdsDictionary: pass
class PdsStream: pass
class PdsNull: pass
class PdsContent: pass
class PdsPageObject: pass
class PdsText: pass
class PdsForm: pass
class PdsPath: pass
class PdsPathPoint: pass
class PdsSoftMask: pass
class PdsImage: pass
class PdsShading: pass
class PdsContentMark: pass
class PdeWordList: pass
class PdeElement: pass
class PdeContainer: pass
class PdeList: pass
class PdeAnnot: pass
class PdeFormField: pass
class PdeImage: pass
class PdeLine: pass
class PdeRect: pass
class PdeHeader: pass
class PdeFooter: pass
class PdeArtifact: pass
class PdeCell: pass
class PdeTable: pass
class PdeToc: pass
class PdeTextRun: pass
class PdeWord: pass
class PdeTextLine: pass
class PdeText: pass
class PdfColorSpace: pass
class PdfColor: pass
class PdfAction: pass
class PdfActionHandler: pass
class PdfAnnot: pass
class PdfLinkAnnot: pass
class PdfMarkupAnnot: pass
class PdfTextAnnot: pass
class PdfTextMarkupAnnot: pass
class PdfWidgetAnnot: pass
class PdfAnnotHandler: pass
class PdfViewDestination: pass
class PdfSecurityHandler: pass
class PdfStandardSecurityHandler: pass
class PdfCustomSecurityHandler: pass
class PdfBaseDigSig: pass
class PdfDigSig: pass
class PdfCustomDigSig: pass
class PdfDocUndo: pass
class PdfDoc: pass
class PdsFileSpec: pass
class PdfDocTemplate: pass
class PdfPageTemplate: pass
class PdfAlternate: pass
class PdfHtmlAlternate: pass
class PdfFont: pass
class PdfFormField: pass
class PdfPage: pass
class PdePageMap: pass
class PdfPageView: pass
class PdfBookmark: pass
class PdfNameTree: pass
class PsRegex: pass
class PsStream: pass
class PsFileStream: pass
class PsMemoryStream: pass
class PsCustomStream: pass
class PdsStructElement: pass
class PdsClassMap: pass
class PdsRoleMap: pass
class PdsStructTree: pass
class PdfConversion: pass
class PdfHtmlConversion: pass
class PdfJsonConversion: pass
class PdfTiffConversion: pass
class PdfSelection: pass
class PsEvent: pass
class PsAuthorization: pass
class PsAccountAuthorization: pass
class PsStandardAuthorization: pass
class PsCommand: pass
class PsProgressControl: pass
class PsRenderDeviceContext: pass
class PsImage: pass
class PsSysFont: pass
class Pdfix: pass
class PdfixPlugin: pass

# class definitions 
class PdsObject(_PdfixBase):
    def __init__(self, _obj):
        super(PdsObject, self).__init__(_obj)

    def GetObjectType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsObjectGetObjectType(self.obj)
        return ret

    def GetId(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsObjectGetId(self.obj)
        return ret

    def GetGenId(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsObjectGetGenId(self.obj)
        return ret

    def GetDoc(self) -> PdfDoc: 
        global PdfixLib
        ret = PdfixLib.PdsObjectGetDoc(self.obj)
        if ret:
            return PdfDoc(ret)
        else:
            return None

    def Clone(self, _clone_indirect: bool) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdsObjectClone(self.obj, _clone_indirect)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def RegisterEvent(self, _type: int, _proc, _data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsObjectRegisterEvent(self.obj, _type, _proc, _data)
        return ret

    def UnregisterEvent(self, _type: int, _proc, _data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsObjectUnregisterEvent(self.obj, _type, _proc, _data)
        return ret

class PdsBoolean(PdsObject):
    def __init__(self, _obj):
        super(PdsBoolean, self).__init__(_obj)

    def GetValue(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsBooleanGetValue(self.obj)
        return ret

class PdsNumber(PdsObject):
    def __init__(self, _obj):
        super(PdsNumber, self).__init__(_obj)

    def IsIntegerValue(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsNumberIsIntegerValue(self.obj)
        return ret

    def GetIntegerValue(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsNumberGetIntegerValue(self.obj)
        return ret

    def GetValue(self) -> float: 
        global PdfixLib
        ret = PdfixLib.PdsNumberGetValue(self.obj)
        return ret

class PdsString(PdsObject):
    def __init__(self, _obj):
        super(PdsString, self).__init__(_obj)

    def GetValue(self, _buffer, _len: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStringGetValue(self.obj, _buffer, _len)
        return ret

    def GetText(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsStringGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStringGetText(self.obj, _buffer, _len)
        return _buffer.value

    def IsHexValue(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStringIsHexValue(self.obj)
        return ret

class PdsName(PdsObject):
    def __init__(self, _obj):
        super(PdsName, self).__init__(_obj)

    def GetValue(self, _buffer, _len: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsNameGetValue(self.obj, _buffer, _len)
        return ret

    def GetText(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsNameGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsNameGetText(self.obj, _buffer, _len)
        return _buffer.value

class PdsArray(PdsObject):
    def __init__(self, _obj):
        super(PdsArray, self).__init__(_obj)

    def GetNumObjects(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsArrayGetNumObjects(self.obj)
        return ret

    def Get(self, _index: int) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdsArrayGet(self.obj, _index)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def Put(self, _index: int, _value: PdsObject) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsArrayPut(self.obj, _index, _value.obj if _value else None)
        return ret

    def PutNumber(self, _index: int, _value: float) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsArrayPutNumber(self.obj, _index, _value)
        return ret

    def PutName(self, _index: int, _value) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsArrayPutName(self.obj, _index, _value)
        return ret

    def PutString(self, _index: int, _value) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsArrayPutString(self.obj, _index, _value)
        return ret

    def Insert(self, _index: int, _value: PdsObject) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsArrayInsert(self.obj, _index, _value.obj if _value else None)
        return ret

    def InsertDict(self, _index: int) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdsArrayInsertDict(self.obj, _index)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def InsertArray(self, _index: int) -> PdsArray: 
        global PdfixLib
        ret = PdfixLib.PdsArrayInsertArray(self.obj, _index)
        if ret:
            return PdsArray(ret)
        else:
            return None

    def RemoveNth(self, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsArrayRemoveNth(self.obj, _index)
        return ret

    def GetDictionary(self, _index: int) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdsArrayGetDictionary(self.obj, _index)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def GetArray(self, _index: int) -> PdsArray: 
        global PdfixLib
        ret = PdfixLib.PdsArrayGetArray(self.obj, _index)
        if ret:
            return PdsArray(ret)
        else:
            return None

    def GetStream(self, _index: int) -> PdsStream: 
        global PdfixLib
        ret = PdfixLib.PdsArrayGetStream(self.obj, _index)
        if ret:
            return PdsStream(ret)
        else:
            return None

    def GetString(self, _index: int, _buffer, _len: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsArrayGetString(self.obj, _index, _buffer, _len)
        return ret

    def GetText(self, _index: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsArrayGetText(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsArrayGetText(self.obj, _index, _buffer, _len)
        return _buffer.value

    def GetNumber(self, _index: int) -> float: 
        global PdfixLib
        ret = PdfixLib.PdsArrayGetNumber(self.obj, _index)
        return ret

    def GetInteger(self, _index: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsArrayGetInteger(self.obj, _index)
        return ret

class PdsDictionary(PdsObject):
    def __init__(self, _obj):
        super(PdsDictionary, self).__init__(_obj)

    def Known(self, _key) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryKnown(self.obj, _key)
        return ret

    def GetNumKeys(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryGetNumKeys(self.obj)
        return ret

    def GetKey(self, _index: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsDictionaryGetKey(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsDictionaryGetKey(self.obj, _index, _buffer, _len)
        return _buffer.value

    def Get(self, _key) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryGet(self.obj, _key)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def Put(self, _key, _value: PdsObject) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryPut(self.obj, _key, _value.obj if _value else None)
        return ret

    def PutBool(self, _key, _value: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryPutBool(self.obj, _key, _value)
        return ret

    def PutName(self, _key, _value) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryPutName(self.obj, _key, _value)
        return ret

    def PutString(self, _key, _value) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryPutString(self.obj, _key, _value)
        return ret

    def PutNumber(self, _key, _value: float) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryPutNumber(self.obj, _key, _value)
        return ret

    def GetRect(self, _key) -> bool: 
        global PdfixLib
        result = PdfRect()
        _rect = result.GetIntStruct()
        PdfixLib.PdsDictionaryGetRect(self.obj, _key, _rect)
        result.SetIntStruct(_rect)
        return result

    def PutRect(self, _key, _rect: PdfRect) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryPutRect(self.obj, _key, _rect.GetIntStruct() if _rect else None)
        return ret

    def GetMatrix(self, _key) -> bool: 
        global PdfixLib
        result = PdfMatrix()
        _matrix = result.GetIntStruct()
        PdfixLib.PdsDictionaryGetMatrix(self.obj, _key, _matrix)
        result.SetIntStruct(_matrix)
        return result

    def PutMatrix(self, _key, _matrix: PdfMatrix) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryPutMatrix(self.obj, _key, _matrix.GetIntStruct() if _matrix else None)
        return ret

    def PutDict(self, _key) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryPutDict(self.obj, _key)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def PutArray(self, _key) -> PdsArray: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryPutArray(self.obj, _key)
        if ret:
            return PdsArray(ret)
        else:
            return None

    def GetDictionary(self, _key) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryGetDictionary(self.obj, _key)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def GetArray(self, _key) -> PdsArray: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryGetArray(self.obj, _key)
        if ret:
            return PdsArray(ret)
        else:
            return None

    def GetStream(self, _key) -> PdsStream: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryGetStream(self.obj, _key)
        if ret:
            return PdsStream(ret)
        else:
            return None

    def GetString(self, _key, _buffer, _len: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryGetString(self.obj, _key, _buffer, _len)
        return ret

    def GetText(self, _key) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsDictionaryGetText(self.obj, _key, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsDictionaryGetText(self.obj, _key, _buffer, _len)
        return _buffer.value

    def GetNumber(self, _key) -> float: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryGetNumber(self.obj, _key)
        return ret

    def GetInteger(self, _key, _default_value: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryGetInteger(self.obj, _key, _default_value)
        return ret

    def GetBoolean(self, _key, _default_value: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryGetBoolean(self.obj, _key, _default_value)
        return ret

    def RemoveKey(self, _key) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsDictionaryRemoveKey(self.obj, _key)
        return ret

class PdsStream(PdsObject):
    def __init__(self, _obj):
        super(PdsStream, self).__init__(_obj)

    def GetStreamDict(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdsStreamGetStreamDict(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def GetRawDataSize(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStreamGetRawDataSize(self.obj)
        return ret

    def IsEof(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStreamIsEof(self.obj)
        return ret

    def GetSize(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStreamGetSize(self.obj)
        return ret

    def Read(self, _offset: int, _buffer, _size: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStreamRead(self.obj, _offset, _buffer, _size)
        return ret

    def GetPos(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStreamGetPos(self.obj)
        return ret

class PdsNull(PdsObject):
    def __init__(self, _obj):
        super(PdsNull, self).__init__(_obj)

class PdsContent(_PdfixBase):
    def __init__(self, _obj):
        super(PdsContent, self).__init__(_obj)

    def AddNewText(self, _index: int, _font: PdfFont, _matrix: PdfMatrix) -> PdsText: 
        global PdfixLib
        ret = PdfixLib.PdsContentAddNewText(self.obj, _index, _font.obj if _font else None, _matrix.GetIntStruct() if _matrix else None)
        if ret:
            return PdsText(ret)
        else:
            return None

    def AddNewPath(self, _index: int, _matrix: PdfMatrix) -> PdsPath: 
        global PdfixLib
        ret = PdfixLib.PdsContentAddNewPath(self.obj, _index, _matrix.GetIntStruct() if _matrix else None)
        if ret:
            return PdsPath(ret)
        else:
            return None

    def AddNewImage(self, _index: int, _image_xobj: PdsStream, _matrix: PdfMatrix) -> PdsImage: 
        global PdfixLib
        ret = PdfixLib.PdsContentAddNewImage(self.obj, _index, _image_xobj.obj if _image_xobj else None, _matrix.GetIntStruct() if _matrix else None)
        if ret:
            return PdsImage(ret)
        else:
            return None

    def AddNewForm(self, _index: int, _form_xobj: PdsStream, _matrix: PdfMatrix) -> PdsForm: 
        global PdfixLib
        ret = PdfixLib.PdsContentAddNewForm(self.obj, _index, _form_xobj.obj if _form_xobj else None, _matrix.GetIntStruct() if _matrix else None)
        if ret:
            return PdsForm(ret)
        else:
            return None

    def RemoveObject(self, _object: PdsPageObject) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsContentRemoveObject(self.obj, _object.obj if _object else None)
        return ret

    def GetNumObjects(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsContentGetNumObjects(self.obj)
        return ret

    def GetObject(self, _index: int) -> PdsPageObject: 
        global PdfixLib
        ret = PdfixLib.PdsContentGetObject(self.obj, _index)
        if ret:
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPageText:
                return PdsText(ret)
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPagePath:
                return PdsPath(ret)
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPageImage:
                return PdsImage(ret)
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPageShading:
                return PdsShading(ret)
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPageForm:
                return PdsForm(ret)
            return PdsPageObject(ret)
        else:
            return None

    def ToObject(self, _doc: PdfDoc, _content_params: PdsContentParams) -> PdsStream: 
        global PdfixLib
        ret = PdfixLib.PdsContentToObject(self.obj, _doc.obj if _doc else None, _content_params.GetIntStruct() if _content_params else None)
        if ret:
            return PdsStream(ret)
        else:
            return None

    def GetPage(self) -> PdfPage: 
        global PdfixLib
        ret = PdfixLib.PdsContentGetPage(self.obj)
        if ret:
            return PdfPage(ret)
        else:
            return None

    def GetForm(self) -> PdsForm: 
        global PdfixLib
        ret = PdfixLib.PdsContentGetForm(self.obj)
        if ret:
            return PdsForm(ret)
        else:
            return None

    def RegisterEvent(self, _type: int, _proc, _data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsContentRegisterEvent(self.obj, _type, _proc, _data)
        return ret

    def UnregisterEvent(self, _type: int, _proc, _data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsContentUnregisterEvent(self.obj, _type, _proc, _data)
        return ret

class PdsPageObject(_PdfixBase):
    def __init__(self, _obj):
        super(PdsPageObject, self).__init__(_obj)

    def GetObjectType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetObjectType(self.obj)
        return ret

    def GetBBox(self): 
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdsPageObjectGetBBox(self.obj, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def GetQuad(self): 
        global PdfixLib
        result = PdfQuad()
        _quad = result.GetIntStruct()
        PdfixLib.PdsPageObjectGetQuad(self.obj, _quad)
        result.SetIntStruct(_quad)
        return result

    def GetId(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetId(self.obj)
        return ret

    def GetStateFlags(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetStateFlags(self.obj)
        return ret

    def SetStateFlags(self, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectSetStateFlags(self.obj, _flags)
        return ret

    def GetStructObject(self, _struct_parent: bool) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetStructObject(self.obj, _struct_parent)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def GetContentMark(self) -> PdsContentMark: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetContentMark(self.obj)
        if ret:
            return PdsContentMark(ret)
        else:
            return None

    def GetMcid(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetMcid(self.obj)
        return ret

    def RemoveTags(self, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectRemoveTags(self.obj, _flags)
        return ret

    def GetPage(self) -> PdfPage: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetPage(self.obj)
        if ret:
            return PdfPage(ret)
        else:
            return None

    def GetContentStreamIndex(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetContentStreamIndex(self.obj)
        return ret

    def GetParentContent(self) -> PdsContent: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetParentContent(self.obj)
        if ret:
            return PdsContent(ret)
        else:
            return None

    def GetGState(self) -> bool: 
        global PdfixLib
        result = PdfGraphicState()
        _g_state = result.GetIntStruct()
        PdfixLib.PdsPageObjectGetGState(self.obj, _g_state)
        result.SetIntStruct(_g_state)
        return result

    def SetGState(self, _g_state: PdfGraphicState) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectSetGState(self.obj, _g_state.GetIntStruct() if _g_state else None)
        return ret

    def TransformCTM(self, _matrix: PdfMatrix) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectTransformCTM(self.obj, _matrix.GetIntStruct() if _matrix else None)
        return ret

    def MoveToObject(self, _ref_obj: PdsPageObject, _after: bool, _dst_tag_index: int, _obj_tag_index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectMoveToObject(self.obj, _ref_obj.obj if _ref_obj else None, _after, _dst_tag_index, _obj_tag_index)
        return ret

    def MoveToContent(self, _content: PdsContent, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectMoveToContent(self.obj, _content.obj if _content else None, _index)
        return ret

    def CopyToContent(self, _content: PdsContent, _index: int) -> PdsPageObject: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectCopyToContent(self.obj, _content.obj if _content else None, _index)
        if ret:
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPageText:
                return PdsText(ret)
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPagePath:
                return PdsPath(ret)
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPageImage:
                return PdsImage(ret)
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPageShading:
                return PdsShading(ret)
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPageForm:
                return PdsForm(ret)
            return PdsPageObject(ret)
        else:
            return None

    def GetDoc(self) -> PdfDoc: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetDoc(self.obj)
        if ret:
            return PdfDoc(ret)
        else:
            return None

    def GetNumEqualTags(self, _object: PdsPageObject) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetNumEqualTags(self.obj, _object.obj if _object else None)
        return ret

    def GetOperatorId(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetOperatorId(self.obj)
        return ret

    def GetContentId(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetContentId(self.obj)
        return ret

    def GetNumContentItemIds(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetNumContentItemIds(self.obj)
        return ret

    def GetContentItemId(self, _level: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectGetContentItemId(self.obj, _level)
        return ret

    def RegisterEvent(self, _type: int, _proc, _data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectRegisterEvent(self.obj, _type, _proc, _data)
        return ret

    def UnregisterEvent(self, _type: int, _proc, _data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPageObjectUnregisterEvent(self.obj, _type, _proc, _data)
        return ret

class PdsText(PdsPageObject):
    def __init__(self, _obj):
        super(PdsText, self).__init__(_obj)

    def GetText(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsTextGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsTextGetText(self.obj, _buffer, _len)
        return _buffer.value

    def GetTextEx(self, _text_flags: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsTextGetTextEx(self.obj, _text_flags, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsTextGetTextEx(self.obj, _text_flags, _buffer, _len)
        return _buffer.value

    def SetText(self, _buffer): 
        global PdfixLib
        ret = PdfixLib.PdsTextSetText(self.obj, _buffer)
        return ret

    def GetTextState(self) -> bool: 
        global PdfixLib
        result = PdfTextState()
        _text_state = result.GetIntStruct()
        PdfixLib.PdsTextGetTextState(self.obj, _text_state)
        result.SetIntStruct(_text_state)
        return result

    def SetTextState(self, _text_state: PdfTextState): 
        global PdfixLib
        ret = PdfixLib.PdsTextSetTextState(self.obj, _text_state.GetIntStruct() if _text_state else None)
        return ret

    def GetTextMatrix(self) -> bool: 
        global PdfixLib
        result = PdfMatrix()
        _matrix = result.GetIntStruct()
        PdfixLib.PdsTextGetTextMatrix(self.obj, _matrix)
        result.SetIntStruct(_matrix)
        return result

    def GetNumChars(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsTextGetNumChars(self.obj)
        return ret

    def GetCharCode(self, _index: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsTextGetCharCode(self.obj, _index)
        return ret

    def GetCharText(self, _index: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsTextGetCharText(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsTextGetCharText(self.obj, _index, _buffer, _len)
        return _buffer.value

    def GetCharBBox(self, _index: int) -> bool: 
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdsTextGetCharBBox(self.obj, _index, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def GetCharQuad(self, _index: int) -> bool: 
        global PdfixLib
        result = PdfQuad()
        _quad = result.GetIntStruct()
        PdfixLib.PdsTextGetCharQuad(self.obj, _index, _quad)
        result.SetIntStruct(_quad)
        return result

    def GetCharAdvanceWidth(self, _index: int) -> float: 
        global PdfixLib
        ret = PdfixLib.PdsTextGetCharAdvanceWidth(self.obj, _index)
        return ret

    def SplitAtChar(self, _index: int) -> PdsText: 
        global PdfixLib
        ret = PdfixLib.PdsTextSplitAtChar(self.obj, _index)
        if ret:
            return PdsText(ret)
        else:
            return None

    def GetCharStateFlags(self, _index: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsTextGetCharStateFlags(self.obj, _index)
        return ret

    def SetCharStateFlags(self, _index: int, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsTextSetCharStateFlags(self.obj, _index, _flags)
        return ret

class PdsForm(PdsPageObject):
    def __init__(self, _obj):
        super(PdsForm, self).__init__(_obj)

    def GetContent(self) -> PdsContent: 
        global PdfixLib
        ret = PdfixLib.PdsFormGetContent(self.obj)
        if ret:
            return PdsContent(ret)
        else:
            return None

    def GetMatrix(self): 
        global PdfixLib
        result = PdfMatrix()
        _matrix = result.GetIntStruct()
        PdfixLib.PdsFormGetMatrix(self.obj, _matrix)
        result.SetIntStruct(_matrix)
        return result

    def GetObject(self) -> PdsStream: 
        global PdfixLib
        ret = PdfixLib.PdsFormGetObject(self.obj)
        if ret:
            return PdsStream(ret)
        else:
            return None

class PdsPath(PdsPageObject):
    def __init__(self, _obj):
        super(PdsPath, self).__init__(_obj)

    def GetNumPathPoints(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsPathGetNumPathPoints(self.obj)
        return ret

    def GetPathPoint(self, _index: int) -> PdsPathPoint: 
        global PdfixLib
        ret = PdfixLib.PdsPathGetPathPoint(self.obj, _index)
        if ret:
            return PdsPathPoint(ret)
        else:
            return None

    def SetStroke(self, _stroke: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPathSetStroke(self.obj, _stroke)
        return ret

    def SetFillType(self, _fill: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPathSetFillType(self.obj, _fill)
        return ret

    def MoveTo(self, _point: PdfPoint) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPathMoveTo(self.obj, _point.GetIntStruct() if _point else None)
        return ret

    def LineTo(self, _point: PdfPoint) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPathLineTo(self.obj, _point.GetIntStruct() if _point else None)
        return ret

    def CurveTo(self, _control_p_1: PdfPoint, _control_p_2: PdfPoint, _point: PdfPoint) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPathCurveTo(self.obj, _control_p_1.GetIntStruct() if _control_p_1 else None, _control_p_2.GetIntStruct() if _control_p_2 else None, _point.GetIntStruct() if _point else None)
        return ret

    def ArcTo(self, _end_p: PdfPoint, _radius_p: PdfPoint, _angle: float, _is_large: bool, _sweep: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPathArcTo(self.obj, _end_p.GetIntStruct() if _end_p else None, _radius_p.GetIntStruct() if _radius_p else None, _angle, _is_large, _sweep)
        return ret

    def ClosePath(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPathClosePath(self.obj)
        return ret

class PdsPathPoint(_PdfixBase):
    def __init__(self, _obj):
        super(PdsPathPoint, self).__init__(_obj)

    def GetType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsPathPointGetType(self.obj)
        return ret

    def GetPoint(self) -> bool: 
        global PdfixLib
        result = PdfPoint()
        _point = result.GetIntStruct()
        PdfixLib.PdsPathPointGetPoint(self.obj, _point)
        result.SetIntStruct(_point)
        return result

    def IsClosed(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsPathPointIsClosed(self.obj)
        return ret

class PdsSoftMask(_PdfixBase):
    def __init__(self, _obj):
        super(PdsSoftMask, self).__init__(_obj)

    def GetDataStm(self) -> PdsStream: 
        global PdfixLib
        ret = PdfixLib.PdsSoftMaskGetDataStm(self.obj)
        if ret:
            return PdsStream(ret)
        else:
            return None

class PdsImage(PdsPageObject):
    def __init__(self, _obj):
        super(PdsImage, self).__init__(_obj)

    def GetDataStm(self) -> PdsStream: 
        global PdfixLib
        ret = PdfixLib.PdsImageGetDataStm(self.obj)
        if ret:
            return PdsStream(ret)
        else:
            return None

    def GetSMask(self) -> PdsSoftMask: 
        global PdfixLib
        ret = PdfixLib.PdsImageGetSMask(self.obj)
        if ret:
            return PdsSoftMask(ret)
        else:
            return None

    def HasSMask(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsImageHasSMask(self.obj)
        return ret

class PdsShading(PdsPageObject):
    def __init__(self, _obj):
        super(PdsShading, self).__init__(_obj)

class PdsContentMark(_PdfixBase):
    def __init__(self, _obj):
        super(PdsContentMark, self).__init__(_obj)

    def GetNumTags(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsContentMarkGetNumTags(self.obj)
        return ret

    def GetTagName(self, _index: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsContentMarkGetTagName(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsContentMarkGetTagName(self.obj, _index, _buffer, _len)
        return _buffer.value

    def SetTagName(self, _index: int, _name) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsContentMarkSetTagName(self.obj, _index, _name)
        return ret

    def GetTagObject(self, _index: int) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdsContentMarkGetTagObject(self.obj, _index)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def SetTagObject(self, _index: int, _object: PdsDictionary, _indirect: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsContentMarkSetTagObject(self.obj, _index, _object.obj if _object else None, _indirect)
        return ret

    def GetTagMcid(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsContentMarkGetTagMcid(self.obj)
        return ret

    def GetTagArtifact(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsContentMarkGetTagArtifact(self.obj)
        return ret

    def AddTag(self, _name, _object: PdsDictionary, _indirect: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsContentMarkAddTag(self.obj, _name, _object.obj if _object else None, _indirect)
        return ret

    def InsertTag(self, _index: int, _name, _object: PdsDictionary, _indirect: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsContentMarkInsertTag(self.obj, _index, _name, _object.obj if _object else None, _indirect)
        return ret

    def RemoveTag(self, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsContentMarkRemoveTag(self.obj, _index)
        return ret

class PdeWordList(_PdfixBase):
    def __init__(self, _obj):
        super(PdeWordList, self).__init__(_obj)

    def GetNumWords(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeWordListGetNumWords(self.obj)
        return ret

    def GetWord(self, _index: int) -> PdeWord: 
        global PdfixLib
        ret = PdfixLib.PdeWordListGetWord(self.obj, _index)
        if ret:
            return PdeWord(ret)
        else:
            return None

    def GetRefNum(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeWordListGetRefNum(self.obj)
        return ret

    def Release(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeWordListRelease(self.obj)
        return ret

class PdeElement(_PdfixBase):
    def __init__(self, _obj):
        super(PdeElement, self).__init__(_obj)

    def GetType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeElementGetType(self.obj)
        return ret

    def GetBBox(self): 
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdeElementGetBBox(self.obj, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def SetBBox(self, _bbox: PdfRect) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeElementSetBBox(self.obj, _bbox.GetIntStruct() if _bbox else None)
        return ret

    def GetQuad(self): 
        global PdfixLib
        result = PdfQuad()
        _quad = result.GetIntStruct()
        PdfixLib.PdeElementGetQuad(self.obj, _quad)
        result.SetIntStruct(_quad)
        return result

    def GetId(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeElementGetId(self.obj)
        return ret

    def GetGraphicState(self) -> bool: 
        global PdfixLib
        result = PdeGraphicState()
        _g_state = result.GetIntStruct()
        PdfixLib.PdeElementGetGraphicState(self.obj, _g_state)
        result.SetIntStruct(_g_state)
        return result

    def GetNumChildren(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeElementGetNumChildren(self.obj)
        return ret

    def GetChild(self, _index: int) -> PdeElement: 
        global PdfixLib
        ret = PdfixLib.PdeElementGetChild(self.obj, _index)
        if ret:
            if PdfixLib.PdeElementGetType(ret) == kPdeText:
                return PdeText(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTextLine:
                return PdeTextLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeWord:
                return PdeWord(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeImage:
                return PdeImage(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeContainer:
                return PdeContainer(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeList:
                return PdeList(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeLine:
                return PdeLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeRect:
                return PdeRect(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeHeader:
                return PdeHeader(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFooter:
                return PdeFooter(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeArtifact:
                return PdeArtifact(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTable:
                return PdeTable(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeCell:
                return PdeCell(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFormField:
                return PdeFormField(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeToc:
                return PdeToc(ret)
            return PdeElement(ret)
        else:
            return None

    def GetAlignment(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeElementGetAlignment(self.obj)
        return ret

    def GetAngle(self) -> float: 
        global PdfixLib
        ret = PdfixLib.PdeElementGetAngle(self.obj)
        return ret

    def SetData(self, _data: int): 
        global PdfixLib
        ret = PdfixLib.PdeElementSetData(self.obj, _data)
        return ret

    def GetData(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeElementGetData(self.obj)
        return ret

    def SetAlt(self, _alt) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeElementSetAlt(self.obj, _alt)
        return ret

    def SetActualText(self, _text) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeElementSetActualText(self.obj, _text)
        return ret

    def GetTag(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdeElementGetTag(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdeElementGetTag(self.obj, _buffer, _len)
        return _buffer.value

    def SetTag(self, _text) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeElementSetTag(self.obj, _text)
        return ret

    def GetTagId(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdeElementGetTagId(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdeElementGetTagId(self.obj, _buffer, _len)
        return _buffer.value

    def SetTagId(self, _id) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeElementSetTagId(self.obj, _id)
        return ret

    def GetFlags(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeElementGetFlags(self.obj)
        return ret

    def SetFlags(self, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeElementSetFlags(self.obj, _flags)
        return ret

    def GetStateFlags(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeElementGetStateFlags(self.obj)
        return ret

    def SetStateFlags(self, _flags: int, _objects: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeElementSetStateFlags(self.obj, _flags, _objects)
        return ret

    def GetNumPageObjects(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeElementGetNumPageObjects(self.obj)
        return ret

    def GetPageObject(self, _index: int) -> PdsPageObject: 
        global PdfixLib
        ret = PdfixLib.PdeElementGetPageObject(self.obj, _index)
        if ret:
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPageText:
                return PdsText(ret)
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPagePath:
                return PdsPath(ret)
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPageImage:
                return PdsImage(ret)
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPageShading:
                return PdsShading(ret)
            if PdfixLib.PdsPageObjectGetObjectType(ret) == kPdsPageForm:
                return PdsForm(ret)
            return PdsPageObject(ret)
        else:
            return None

    def GetPageMap(self) -> PdePageMap: 
        global PdfixLib
        ret = PdfixLib.PdeElementGetPageMap(self.obj)
        if ret:
            return PdePageMap(ret)
        else:
            return None

    def GetLabelType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeElementGetLabelType(self.obj)
        return ret

    def SetLabelType(self, _type: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeElementSetLabelType(self.obj, _type)
        return ret

class PdeContainer(PdeElement):
    def __init__(self, _obj):
        super(PdeContainer, self).__init__(_obj)

class PdeList(PdeElement):
    def __init__(self, _obj):
        super(PdeList, self).__init__(_obj)

class PdeAnnot(PdeElement):
    def __init__(self, _obj):
        super(PdeAnnot, self).__init__(_obj)

    def GetAnnot(self) -> PdfAnnot: 
        global PdfixLib
        ret = PdfixLib.PdeAnnotGetAnnot(self.obj)
        if ret:
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotText:
                return PdfTextAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLink:
                return PdfLinkAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFreeText:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquare:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCircle:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolygon:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolyLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotHighlight:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotUnderline:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquiggly:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStrikeOut:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStamp:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCaret:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotInk:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPopup:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFileAttachment:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSound:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotMovie:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWidget:
                return PdfWidgetAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotScreen:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPrinterMark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotTrapNet:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWatermark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnot3D:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotRedact:
                return PdfAnnot(ret)
            return PdfAnnot(ret)
        else:
            return None

class PdeFormField(PdeAnnot):
    def __init__(self, _obj):
        super(PdeFormField, self).__init__(_obj)

class PdeImage(PdeContainer):
    def __init__(self, _obj):
        super(PdeImage, self).__init__(_obj)

    def GetImageType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeImageGetImageType(self.obj)
        return ret

    def GetCaption(self) -> PdeElement: 
        global PdfixLib
        ret = PdfixLib.PdeImageGetCaption(self.obj)
        if ret:
            if PdfixLib.PdeElementGetType(ret) == kPdeText:
                return PdeText(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTextLine:
                return PdeTextLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeWord:
                return PdeWord(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeImage:
                return PdeImage(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeContainer:
                return PdeContainer(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeList:
                return PdeList(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeLine:
                return PdeLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeRect:
                return PdeRect(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeHeader:
                return PdeHeader(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFooter:
                return PdeFooter(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeArtifact:
                return PdeArtifact(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTable:
                return PdeTable(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeCell:
                return PdeCell(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFormField:
                return PdeFormField(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeToc:
                return PdeToc(ret)
            return PdeElement(ret)
        else:
            return None

class PdeLine(PdeElement):
    def __init__(self, _obj):
        super(PdeLine, self).__init__(_obj)

class PdeRect(PdeContainer):
    def __init__(self, _obj):
        super(PdeRect, self).__init__(_obj)

class PdeHeader(PdeContainer):
    def __init__(self, _obj):
        super(PdeHeader, self).__init__(_obj)

class PdeFooter(PdeContainer):
    def __init__(self, _obj):
        super(PdeFooter, self).__init__(_obj)

class PdeArtifact(PdeContainer):
    def __init__(self, _obj):
        super(PdeArtifact, self).__init__(_obj)

class PdeCell(PdeContainer):
    def __init__(self, _obj):
        super(PdeCell, self).__init__(_obj)

    def GetRowNum(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeCellGetRowNum(self.obj)
        return ret

    def SetRowNum(self, _row: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeCellSetRowNum(self.obj, _row)
        return ret

    def GetColNum(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeCellGetColNum(self.obj)
        return ret

    def SetColNum(self, _col: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeCellSetColNum(self.obj, _col)
        return ret

    def GetHeader(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeCellGetHeader(self.obj)
        return ret

    def SetHeader(self, _header: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeCellSetHeader(self.obj, _header)
        return ret

    def GetHeaderScope(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeCellGetHeaderScope(self.obj)
        return ret

    def SetHeaderScope(self, _scope: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeCellSetHeaderScope(self.obj, _scope)
        return ret

    def GetRowSpan(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeCellGetRowSpan(self.obj)
        return ret

    def SetRowSpan(self, _span: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeCellSetRowSpan(self.obj, _span)
        return ret

    def GetColSpan(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeCellGetColSpan(self.obj)
        return ret

    def SetColSpan(self, _span: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeCellSetColSpan(self.obj, _span)
        return ret

    def HasBorderGraphicState(self, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeCellHasBorderGraphicState(self.obj, _index)
        return ret

    def GetSpanCell(self) -> PdeCell: 
        global PdfixLib
        ret = PdfixLib.PdeCellGetSpanCell(self.obj)
        if ret:
            return PdeCell(ret)
        else:
            return None

    def GetNumAssociatedHeaders(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeCellGetNumAssociatedHeaders(self.obj)
        return ret

    def GetAssociatedHeader(self, _index: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdeCellGetAssociatedHeader(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdeCellGetAssociatedHeader(self.obj, _index, _buffer, _len)
        return _buffer.value

    def AddAssociatedHeader(self, _id) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeCellAddAssociatedHeader(self.obj, _id)
        return ret

    def RemoveAssociatedHeader(self, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeCellRemoveAssociatedHeader(self.obj, _index)
        return ret

class PdeTable(PdeContainer):
    def __init__(self, _obj):
        super(PdeTable, self).__init__(_obj)

    def GetNumRows(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeTableGetNumRows(self.obj)
        return ret

    def SetNumRows(self, _num: int): 
        global PdfixLib
        ret = PdfixLib.PdeTableSetNumRows(self.obj, _num)
        return ret

    def GetNumCols(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeTableGetNumCols(self.obj)
        return ret

    def SetNumCols(self, _num: int): 
        global PdfixLib
        ret = PdfixLib.PdeTableSetNumCols(self.obj, _num)
        return ret

    def GetCell(self, _row: int, _col: int) -> PdeCell: 
        global PdfixLib
        ret = PdfixLib.PdeTableGetCell(self.obj, _row, _col)
        if ret:
            return PdeCell(ret)
        else:
            return None

    def GetRowAlignment(self, _row: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeTableGetRowAlignment(self.obj, _row)
        return ret

    def GetColAlignment(self, _col: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeTableGetColAlignment(self.obj, _col)
        return ret

    def GetCaption(self) -> PdeElement: 
        global PdfixLib
        ret = PdfixLib.PdeTableGetCaption(self.obj)
        if ret:
            if PdfixLib.PdeElementGetType(ret) == kPdeText:
                return PdeText(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTextLine:
                return PdeTextLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeWord:
                return PdeWord(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeImage:
                return PdeImage(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeContainer:
                return PdeContainer(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeList:
                return PdeList(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeLine:
                return PdeLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeRect:
                return PdeRect(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeHeader:
                return PdeHeader(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFooter:
                return PdeFooter(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeArtifact:
                return PdeArtifact(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTable:
                return PdeTable(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeCell:
                return PdeCell(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFormField:
                return PdeFormField(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeToc:
                return PdeToc(ret)
            return PdeElement(ret)
        else:
            return None

    def GetTableType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeTableGetTableType(self.obj)
        return ret

class PdeToc(PdeTable):
    def __init__(self, _obj):
        super(PdeToc, self).__init__(_obj)

class PdeTextRun(PdeElement):
    def __init__(self, _obj):
        super(PdeTextRun, self).__init__(_obj)

    def GetTextObject(self) -> PdsText: 
        global PdfixLib
        ret = PdfixLib.PdeTextRunGetTextObject(self.obj)
        if ret:
            return PdsText(ret)
        else:
            return None

    def GetFirstCharIndex(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeTextRunGetFirstCharIndex(self.obj)
        return ret

    def GetLastCharIndex(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeTextRunGetLastCharIndex(self.obj)
        return ret

class PdeWord(PdeElement):
    def __init__(self, _obj):
        super(PdeWord, self).__init__(_obj)

    def GetText(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdeWordGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdeWordGetText(self.obj, _buffer, _len)
        return _buffer.value

    def HasTextState(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeWordHasTextState(self.obj)
        return ret

    def GetTextState(self): 
        global PdfixLib
        result = PdfTextState()
        _text_state = result.GetIntStruct()
        PdfixLib.PdeWordGetTextState(self.obj, _text_state)
        result.SetIntStruct(_text_state)
        return result

    def GetNumChars(self, _include_spaces: bool) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeWordGetNumChars(self.obj, _include_spaces)
        return ret

    def GetCharCode(self, _index: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeWordGetCharCode(self.obj, _index)
        return ret

    def GetCharText(self, _index: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdeWordGetCharText(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdeWordGetCharText(self.obj, _index, _buffer, _len)
        return _buffer.value

    def GetCharTextState(self, _index: int): 
        global PdfixLib
        result = PdfTextState()
        _text_state = result.GetIntStruct()
        PdfixLib.PdeWordGetCharTextState(self.obj, _index, _text_state)
        result.SetIntStruct(_text_state)
        return result

    def GetCharBBox(self, _index: int): 
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdeWordGetCharBBox(self.obj, _index, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def GetWordFlags(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeWordGetWordFlags(self.obj)
        return ret

    def GetBackground(self) -> PdeElement: 
        global PdfixLib
        ret = PdfixLib.PdeWordGetBackground(self.obj)
        if ret:
            if PdfixLib.PdeElementGetType(ret) == kPdeText:
                return PdeText(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTextLine:
                return PdeTextLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeWord:
                return PdeWord(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeImage:
                return PdeImage(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeContainer:
                return PdeContainer(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeList:
                return PdeList(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeLine:
                return PdeLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeRect:
                return PdeRect(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeHeader:
                return PdeHeader(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFooter:
                return PdeFooter(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeArtifact:
                return PdeArtifact(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTable:
                return PdeTable(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeCell:
                return PdeCell(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFormField:
                return PdeFormField(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeToc:
                return PdeToc(ret)
            return PdeElement(ret)
        else:
            return None

    def GetOrigin(self): 
        global PdfixLib
        result = PdfPoint()
        _point = result.GetIntStruct()
        PdfixLib.PdeWordGetOrigin(self.obj, _point)
        result.SetIntStruct(_point)
        return result

    def GetNumTextRuns(self, _include_spaces: bool) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeWordGetNumTextRuns(self.obj, _include_spaces)
        return ret

    def GetTextRun(self, _index: int) -> PdeTextRun: 
        global PdfixLib
        ret = PdfixLib.PdeWordGetTextRun(self.obj, _index)
        if ret:
            return PdeTextRun(ret)
        else:
            return None

    def GetCharStateFlags(self, _index: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeWordGetCharStateFlags(self.obj, _index)
        return ret

class PdeTextLine(PdeElement):
    def __init__(self, _obj):
        super(PdeTextLine, self).__init__(_obj)

    def GetText(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdeTextLineGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdeTextLineGetText(self.obj, _buffer, _len)
        return _buffer.value

    def HasTextState(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeTextLineHasTextState(self.obj)
        return ret

    def GetTextState(self): 
        global PdfixLib
        result = PdfTextState()
        _text_state = result.GetIntStruct()
        PdfixLib.PdeTextLineGetTextState(self.obj, _text_state)
        result.SetIntStruct(_text_state)
        return result

    def GetNumWords(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeTextLineGetNumWords(self.obj)
        return ret

    def GetWord(self, _index: int) -> PdeWord: 
        global PdfixLib
        ret = PdfixLib.PdeTextLineGetWord(self.obj, _index)
        if ret:
            return PdeWord(ret)
        else:
            return None

    def GetTextLineFlags(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeTextLineGetTextLineFlags(self.obj)
        return ret

class PdeText(PdeElement):
    def __init__(self, _obj):
        super(PdeText, self).__init__(_obj)

    def GetText(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdeTextGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdeTextGetText(self.obj, _buffer, _len)
        return _buffer.value

    def HasTextState(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeTextHasTextState(self.obj)
        return ret

    def GetTextState(self): 
        global PdfixLib
        result = PdfTextState()
        _text_state = result.GetIntStruct()
        PdfixLib.PdeTextGetTextState(self.obj, _text_state)
        result.SetIntStruct(_text_state)
        return result

    def GetNumTextLines(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeTextGetNumTextLines(self.obj)
        return ret

    def GetTextLine(self, _index: int) -> PdeTextLine: 
        global PdfixLib
        ret = PdfixLib.PdeTextGetTextLine(self.obj, _index)
        if ret:
            return PdeTextLine(ret)
        else:
            return None

    def GetNumWords(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeTextGetNumWords(self.obj)
        return ret

    def GetWord(self, _index: int) -> PdeWord: 
        global PdfixLib
        ret = PdfixLib.PdeTextGetWord(self.obj, _index)
        if ret:
            return PdeWord(ret)
        else:
            return None

    def GetLineSpacing(self) -> float: 
        global PdfixLib
        ret = PdfixLib.PdeTextGetLineSpacing(self.obj)
        return ret

    def GetIndent(self) -> float: 
        global PdfixLib
        ret = PdfixLib.PdeTextGetIndent(self.obj)
        return ret

    def GetTextStyle(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeTextGetTextStyle(self.obj)
        return ret

    def SetTextStyle(self, _style: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeTextSetTextStyle(self.obj, _style)
        return ret

    def GetTextFlags(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdeTextGetTextFlags(self.obj)
        return ret

    def SetTextFlags(self, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdeTextSetTextFlags(self.obj, _flags)
        return ret

class PdfColorSpace(_PdfixBase):
    def __init__(self, _obj):
        super(PdfColorSpace, self).__init__(_obj)

    def GetName(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfColorSpaceGetName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfColorSpaceGetName(self.obj, _buffer, _len)
        return _buffer.value

    def GetFamilyType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfColorSpaceGetFamilyType(self.obj)
        return ret

    def GetNumComps(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfColorSpaceGetNumComps(self.obj)
        return ret

    def CreateColor(self) -> PdfColor: 
        global PdfixLib
        ret = PdfixLib.PdfColorSpaceCreateColor(self.obj)
        if ret:
            return PdfColor(ret)
        else:
            return None

class PdfColor(_PdfixBase):
    def __init__(self, _obj):
        super(PdfColor, self).__init__(_obj)

    def GetColorSpace(self) -> PdfColorSpace: 
        global PdfixLib
        ret = PdfixLib.PdfColorGetColorSpace(self.obj)
        if ret:
            return PdfColorSpace(ret)
        else:
            return None

    def SetColorSpace(self, _color_space: PdfColorSpace): 
        global PdfixLib
        ret = PdfixLib.PdfColorSetColorSpace(self.obj, _color_space.obj if _color_space else None)
        return ret

    def GetValue(self, _index: int) -> float: 
        global PdfixLib
        ret = PdfixLib.PdfColorGetValue(self.obj, _index)
        return ret

    def SetValue(self, _index: int, _value: float): 
        global PdfixLib
        ret = PdfixLib.PdfColorSetValue(self.obj, _index, _value)
        return ret

    def GetRGB(self) -> bool: 
        global PdfixLib
        result = PdfRGB()
        _rgb = result.GetIntStruct()
        PdfixLib.PdfColorGetRGB(self.obj, _rgb)
        result.SetIntStruct(_rgb)
        return result

    def GetCMYK(self) -> bool: 
        global PdfixLib
        result = PdfCMYK()
        _cmyk = result.GetIntStruct()
        PdfixLib.PdfColorGetCMYK(self.obj, _cmyk)
        result.SetIntStruct(_cmyk)
        return result

    def GetGrayscale(self) -> bool: 
        global PdfixLib
        result = PdfGray()
        _gray = result.GetIntStruct()
        PdfixLib.PdfColorGetGrayscale(self.obj, _gray)
        result.SetIntStruct(_gray)
        return result

    def Destroy(self): 
        global PdfixLib
        ret = PdfixLib.PdfColorDestroy(self.obj)
        return ret

class PdfAction(_PdfixBase):
    def __init__(self, _obj):
        super(PdfAction, self).__init__(_obj)

    def GetSubtype(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfActionGetSubtype(self.obj)
        return ret

    def GetJavaScript(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfActionGetJavaScript(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfActionGetJavaScript(self.obj, _buffer, _len)
        return _buffer.value

    def GetObject(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdfActionGetObject(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def GetDestFile(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfActionGetDestFile(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfActionGetDestFile(self.obj, _buffer, _len)
        return _buffer.value

    def GetViewDestination(self) -> PdfViewDestination: 
        global PdfixLib
        ret = PdfixLib.PdfActionGetViewDestination(self.obj)
        if ret:
            return PdfViewDestination(ret)
        else:
            return None

    def SetViewDestination(self, _view_dest: PdfViewDestination) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfActionSetViewDestination(self.obj, _view_dest.obj if _view_dest else None)
        return ret

    def CanCopy(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfActionCanCopy(self.obj)
        return ret

    def CanPaste(self, _dest_doc: PdfDoc, _data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfActionCanPaste(self.obj, _dest_doc.obj if _dest_doc else None, _data)
        return ret

    def Copy(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfActionCopy(self.obj)
        return ret

    def Paste(self, _dest_doc: PdfDoc, _data: int) -> PdfAction: 
        global PdfixLib
        ret = PdfixLib.PdfActionPaste(self.obj, _dest_doc.obj if _dest_doc else None, _data)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def DestroyClipboardData(self, _data: int): 
        global PdfixLib
        ret = PdfixLib.PdfActionDestroyClipboardData(self.obj, _data)
        return ret

    def GetNumChildren(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfActionGetNumChildren(self.obj)
        return ret

    def GetChild(self, _index: int) -> PdfAction: 
        global PdfixLib
        ret = PdfixLib.PdfActionGetChild(self.obj, _index)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def RemoveChild(self, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfActionRemoveChild(self.obj, _index)
        return ret

class PdfActionHandler(_PdfixBase):
    def __init__(self, _obj):
        super(PdfActionHandler, self).__init__(_obj)

    def GetType(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfActionHandlerGetType(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfActionHandlerGetType(self.obj, _buffer, _len)
        return _buffer.value

    def Destroy(self): 
        global PdfixLib
        ret = PdfixLib.PdfActionHandlerDestroy(self.obj)
        return ret

    def SetCanCopyProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfActionHandlerSetCanCopyProc(self.obj, _proc)
        return ret

    def SetCopyProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfActionHandlerSetCopyProc(self.obj, _proc)
        return ret

    def SetCanPasteProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfActionHandlerSetCanPasteProc(self.obj, _proc)
        return ret

    def SetPasteProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfActionHandlerSetPasteProc(self.obj, _proc)
        return ret

    def SetDestroyDataProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfActionHandlerSetDestroyDataProc(self.obj, _proc)
        return ret

    def SetDestroyProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfActionHandlerSetDestroyProc(self.obj, _proc)
        return ret

class PdfAnnot(_PdfixBase):
    def __init__(self, _obj):
        super(PdfAnnot, self).__init__(_obj)

    def GetSubtype(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotGetSubtype(self.obj)
        return ret

    def GetFlags(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotGetFlags(self.obj)
        return ret

    def SetFlags(self, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotSetFlags(self.obj, _flags)
        return ret

    def GetAppearance(self): 
        global PdfixLib
        result = PdfAnnotAppearance()
        _appearance = result.GetIntStruct()
        PdfixLib.PdfAnnotGetAppearance(self.obj, _appearance)
        result.SetIntStruct(_appearance)
        return result

    def GetAppearanceXObject(self, _mode: int) -> PdsStream: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotGetAppearanceXObject(self.obj, _mode)
        if ret:
            return PdsStream(ret)
        else:
            return None

    def SetAppearanceFromXObject(self, _xobj: PdsStream, _mode: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotSetAppearanceFromXObject(self.obj, _xobj.obj if _xobj else None, _mode)
        return ret

    def RefreshAppearance(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotRefreshAppearance(self.obj)
        return ret

    def GetBBox(self): 
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdfAnnotGetBBox(self.obj, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def PointInAnnot(self, _point: PdfPoint) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotPointInAnnot(self.obj, _point.GetIntStruct() if _point else None)
        return ret

    def RectInAnnot(self, _rect: PdfRect) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotRectInAnnot(self.obj, _rect.GetIntStruct() if _rect else None)
        return ret

    def GetStructObject(self, _struct_parent: bool) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotGetStructObject(self.obj, _struct_parent)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def GetObject(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotGetObject(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def NotifyWillChange(self, _key): 
        global PdfixLib
        ret = PdfixLib.PdfAnnotNotifyWillChange(self.obj, _key)
        return ret

    def NotifyDidChange(self, _key, _err: int): 
        global PdfixLib
        ret = PdfixLib.PdfAnnotNotifyDidChange(self.obj, _key, _err)
        return ret

    def IsValid(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotIsValid(self.obj)
        return ret

    def IsMarkup(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotIsMarkup(self.obj)
        return ret

    def CanCopy(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotCanCopy(self.obj)
        return ret

    def CanPaste(self, _dest_page: PdfPage, _center: PdfPoint, _data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotCanPaste(self.obj, _dest_page.obj if _dest_page else None, _center.GetIntStruct() if _center else None, _data)
        return ret

    def Copy(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotCopy(self.obj)
        return ret

    def Paste(self, _dest_page: PdfPage, _center: PdfPoint, _data: int) -> PdfAnnot: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotPaste(self.obj, _dest_page.obj if _dest_page else None, _center.GetIntStruct() if _center else None, _data)
        if ret:
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotText:
                return PdfTextAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLink:
                return PdfLinkAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFreeText:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquare:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCircle:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolygon:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolyLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotHighlight:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotUnderline:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquiggly:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStrikeOut:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStamp:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCaret:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotInk:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPopup:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFileAttachment:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSound:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotMovie:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWidget:
                return PdfWidgetAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotScreen:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPrinterMark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotTrapNet:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWatermark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnot3D:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotRedact:
                return PdfAnnot(ret)
            return PdfAnnot(ret)
        else:
            return None

    def DestroyClipboardData(self, _data: int): 
        global PdfixLib
        ret = PdfixLib.PdfAnnotDestroyClipboardData(self.obj, _data)
        return ret

    def GetStateFlags(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotGetStateFlags(self.obj)
        return ret

    def SetStateFlags(self, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotSetStateFlags(self.obj, _flags)
        return ret

    def GetPageObject(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdfAnnotGetPageObject(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

class PdfLinkAnnot(PdfAnnot):
    def __init__(self, _obj):
        super(PdfLinkAnnot, self).__init__(_obj)

    def GetNumQuads(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfLinkAnnotGetNumQuads(self.obj)
        return ret

    def GetQuad(self, _index: int): 
        global PdfixLib
        result = PdfQuad()
        _quad = result.GetIntStruct()
        PdfixLib.PdfLinkAnnotGetQuad(self.obj, _index, _quad)
        result.SetIntStruct(_quad)
        return result

    def AddQuad(self, _quad: PdfQuad) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfLinkAnnotAddQuad(self.obj, _quad.GetIntStruct() if _quad else None)
        return ret

    def RemoveQuad(self, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfLinkAnnotRemoveQuad(self.obj, _index)
        return ret

    def GetAction(self) -> PdfAction: 
        global PdfixLib
        ret = PdfixLib.PdfLinkAnnotGetAction(self.obj)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def SetAction(self, _action: PdfAction) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfLinkAnnotSetAction(self.obj, _action.obj if _action else None)
        return ret

class PdfMarkupAnnot(PdfAnnot):
    def __init__(self, _obj):
        super(PdfMarkupAnnot, self).__init__(_obj)

    def GetContents(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfMarkupAnnotGetContents(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfMarkupAnnotGetContents(self.obj, _buffer, _len)
        return _buffer.value

    def SetContents(self, _contents) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfMarkupAnnotSetContents(self.obj, _contents)
        return ret

    def GetAuthor(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfMarkupAnnotGetAuthor(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfMarkupAnnotGetAuthor(self.obj, _buffer, _len)
        return _buffer.value

    def SetAuthor(self, _author) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfMarkupAnnotSetAuthor(self.obj, _author)
        return ret

    def GetNumReplies(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfMarkupAnnotGetNumReplies(self.obj)
        return ret

    def GetReply(self, _index: int) -> PdfAnnot: 
        global PdfixLib
        ret = PdfixLib.PdfMarkupAnnotGetReply(self.obj, _index)
        if ret:
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotText:
                return PdfTextAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLink:
                return PdfLinkAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFreeText:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquare:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCircle:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolygon:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolyLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotHighlight:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotUnderline:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquiggly:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStrikeOut:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStamp:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCaret:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotInk:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPopup:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFileAttachment:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSound:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotMovie:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWidget:
                return PdfWidgetAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotScreen:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPrinterMark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotTrapNet:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWatermark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnot3D:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotRedact:
                return PdfAnnot(ret)
            return PdfAnnot(ret)
        else:
            return None

    def AddReply(self, _author, _text) -> PdfAnnot: 
        global PdfixLib
        ret = PdfixLib.PdfMarkupAnnotAddReply(self.obj, _author, _text)
        if ret:
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotText:
                return PdfTextAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLink:
                return PdfLinkAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFreeText:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquare:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCircle:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolygon:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolyLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotHighlight:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotUnderline:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquiggly:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStrikeOut:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStamp:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCaret:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotInk:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPopup:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFileAttachment:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSound:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotMovie:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWidget:
                return PdfWidgetAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotScreen:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPrinterMark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotTrapNet:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWatermark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnot3D:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotRedact:
                return PdfAnnot(ret)
            return PdfAnnot(ret)
        else:
            return None

class PdfTextAnnot(PdfMarkupAnnot):
    def __init__(self, _obj):
        super(PdfTextAnnot, self).__init__(_obj)

class PdfTextMarkupAnnot(PdfMarkupAnnot):
    def __init__(self, _obj):
        super(PdfTextMarkupAnnot, self).__init__(_obj)

    def GetNumQuads(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfTextMarkupAnnotGetNumQuads(self.obj)
        return ret

    def GetQuad(self, _index: int): 
        global PdfixLib
        result = PdfQuad()
        _quad = result.GetIntStruct()
        PdfixLib.PdfTextMarkupAnnotGetQuad(self.obj, _index, _quad)
        result.SetIntStruct(_quad)
        return result

    def AddQuad(self, _quad: PdfQuad) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfTextMarkupAnnotAddQuad(self.obj, _quad.GetIntStruct() if _quad else None)
        return ret

    def RemoveQuad(self, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfTextMarkupAnnotRemoveQuad(self.obj, _index)
        return ret

class PdfWidgetAnnot(PdfAnnot):
    def __init__(self, _obj):
        super(PdfWidgetAnnot, self).__init__(_obj)

    def GetCaption(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfWidgetAnnotGetCaption(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfWidgetAnnotGetCaption(self.obj, _buffer, _len)
        return _buffer.value

    def GetFontName(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfWidgetAnnotGetFontName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfWidgetAnnotGetFontName(self.obj, _buffer, _len)
        return _buffer.value

    def GetAction(self) -> PdfAction: 
        global PdfixLib
        ret = PdfixLib.PdfWidgetAnnotGetAction(self.obj)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def SetAction(self, _action: PdfAction) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfWidgetAnnotSetAction(self.obj, _action.obj if _action else None)
        return ret

    def GetAAction(self, _event: int) -> PdfAction: 
        global PdfixLib
        ret = PdfixLib.PdfWidgetAnnotGetAAction(self.obj, _event)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def GetFormField(self) -> PdfFormField: 
        global PdfixLib
        ret = PdfixLib.PdfWidgetAnnotGetFormField(self.obj)
        if ret:
            return PdfFormField(ret)
        else:
            return None

class PdfAnnotHandler(_PdfixBase):
    def __init__(self, _obj):
        super(PdfAnnotHandler, self).__init__(_obj)

    def GetType(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfAnnotHandlerGetType(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfAnnotHandlerGetType(self.obj, _buffer, _len)
        return _buffer.value

    def Destroy(self): 
        global PdfixLib
        ret = PdfixLib.PdfAnnotHandlerDestroy(self.obj)
        return ret

    def SetCanCopyProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfAnnotHandlerSetCanCopyProc(self.obj, _proc)
        return ret

    def SetCopyProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfAnnotHandlerSetCopyProc(self.obj, _proc)
        return ret

    def SetCanPasteProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfAnnotHandlerSetCanPasteProc(self.obj, _proc)
        return ret

    def SetPasteProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfAnnotHandlerSetPasteProc(self.obj, _proc)
        return ret

    def SetDestroyDataProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfAnnotHandlerSetDestroyDataProc(self.obj, _proc)
        return ret

    def SetDestroyProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfAnnotHandlerSetDestroyProc(self.obj, _proc)
        return ret

class PdfViewDestination(_PdfixBase):
    def __init__(self, _obj):
        super(PdfViewDestination, self).__init__(_obj)

    def GetPageNum(self, _doc: PdfDoc) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfViewDestinationGetPageNum(self.obj, _doc.obj if _doc else None)
        return ret

    def GetFitType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfViewDestinationGetFitType(self.obj)
        return ret

    def GetBBox(self): 
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdfViewDestinationGetBBox(self.obj, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def GetZoom(self) -> float: 
        global PdfixLib
        ret = PdfixLib.PdfViewDestinationGetZoom(self.obj)
        return ret

    def GetObject(self) -> PdsArray: 
        global PdfixLib
        ret = PdfixLib.PdfViewDestinationGetObject(self.obj)
        if ret:
            return PdsArray(ret)
        else:
            return None

class PdfSecurityHandler(_PdfixBase):
    def __init__(self, _obj):
        super(PdfSecurityHandler, self).__init__(_obj)

    def GetFilter(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfSecurityHandlerGetFilter(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfSecurityHandlerGetFilter(self.obj, _buffer, _len)
        return _buffer.value

    def Destroy(self): 
        global PdfixLib
        ret = PdfixLib.PdfSecurityHandlerDestroy(self.obj)
        return ret

class PdfStandardSecurityHandler(PdfSecurityHandler):
    def __init__(self, _obj):
        super(PdfStandardSecurityHandler, self).__init__(_obj)

    def SetPassword(self, _password, _level: int): 
        global PdfixLib
        ret = PdfixLib.PdfStandardSecurityHandlerSetPassword(self.obj, _password, _level)
        return ret

    def HasPassword(self, _level: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfStandardSecurityHandlerHasPassword(self.obj, _level)
        return ret

    def GetParams(self) -> bool: 
        global PdfixLib
        result = PdfStandardSecurityParams()
        _params = result.GetIntStruct()
        PdfixLib.PdfStandardSecurityHandlerGetParams(self.obj, _params)
        result.SetIntStruct(_params)
        return result

class PdfCustomSecurityHandler(PdfSecurityHandler):
    def __init__(self, _obj):
        super(PdfCustomSecurityHandler, self).__init__(_obj)

    def SetAuthorizationData(self, _data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfCustomSecurityHandlerSetAuthorizationData(self.obj, _data)
        return ret

    def SetDestroyProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfCustomSecurityHandlerSetDestroyProc(self.obj, _proc)
        return ret

    def SetSetAuthoziationDataProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfCustomSecurityHandlerSetSetAuthoziationDataProc(self.obj, _proc)
        return ret

    def SetOnInitProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfCustomSecurityHandlerSetOnInitProc(self.obj, _proc)
        return ret

    def SetGetPermissionsProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfCustomSecurityHandlerSetGetPermissionsProc(self.obj, _proc)
        return ret

    def SetIsMetadataEncryptedProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfCustomSecurityHandlerSetIsMetadataEncryptedProc(self.obj, _proc)
        return ret

    def SetUpdateEncryptDictProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfCustomSecurityHandlerSetUpdateEncryptDictProc(self.obj, _proc)
        return ret

    def SetAuthorizeOwnerProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfCustomSecurityHandlerSetAuthorizeOwnerProc(self.obj, _proc)
        return ret

    def SetGetDecryptSizeProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfCustomSecurityHandlerSetGetDecryptSizeProc(self.obj, _proc)
        return ret

    def SetDecryptContentProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfCustomSecurityHandlerSetDecryptContentProc(self.obj, _proc)
        return ret

    def SetGetEncryptSizeProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfCustomSecurityHandlerSetGetEncryptSizeProc(self.obj, _proc)
        return ret

    def SetEncryptContentProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PdfCustomSecurityHandlerSetEncryptContentProc(self.obj, _proc)
        return ret

class PdfBaseDigSig(_PdfixBase):
    def __init__(self, _obj):
        super(PdfBaseDigSig, self).__init__(_obj)

    def Destroy(self): 
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigDestroy(self.obj)
        return ret

    def SetReason(self, _reason) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigSetReason(self.obj, _reason)
        return ret

    def SetLocation(self, _location) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigSetLocation(self.obj, _location)
        return ret

    def SetContactInfo(self, _contact) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigSetContactInfo(self.obj, _contact)
        return ret

    def SetName(self, _name) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigSetName(self.obj, _name)
        return ret

    def SetTimeStampServer(self, _url, _user_name, _password) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigSetTimeStampServer(self.obj, _url, _user_name, _password)
        return ret

    def SignDoc(self, _doc: PdfDoc, _path) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfBaseDigSigSignDoc(self.obj, _doc.obj if _doc else None, _path)
        return ret

class PdfDigSig(PdfBaseDigSig):
    def __init__(self, _obj):
        super(PdfDigSig, self).__init__(_obj)

    def SetPfxFile(self, _pfx_file, _pfx_password) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDigSigSetPfxFile(self.obj, _pfx_file, _pfx_password)
        return ret

class PdfCustomDigSig(PdfBaseDigSig):
    def __init__(self, _obj):
        super(PdfCustomDigSig, self).__init__(_obj)

    def RegisterDigestDataProc(self, _proc, _data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfCustomDigSigRegisterDigestDataProc(self.obj, _proc, _data)
        return ret

class PdfDocUndo(_PdfixBase):
    def __init__(self, _obj):
        super(PdfDocUndo, self).__init__(_obj)

    def BeginOperation(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocUndoBeginOperation(self.obj)
        return ret

    def EndOperation(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocUndoEndOperation(self.obj)
        return ret

    def GetNumEntries(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocUndoGetNumEntries(self.obj)
        return ret

    def Execute(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocUndoExecute(self.obj)
        return ret

    def GetTitle(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfDocUndoGetTitle(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfDocUndoGetTitle(self.obj, _buffer, _len)
        return _buffer.value

    def GetData(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocUndoGetData(self.obj)
        return ret

class PdfDoc(_PdfixBase):
    def __init__(self, _obj):
        super(PdfDoc, self).__init__(_obj)

    def Save(self, _path, _save_flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocSave(self.obj, _path, _save_flags)
        return ret

    def SaveToStream(self, _stream: PsStream, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocSaveToStream(self.obj, _stream.obj if _stream else None, _flags)
        return ret

    def Close(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocClose(self.obj)
        return ret

    def Authorize(self, _perm: int, _callback, _client_data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocAuthorize(self.obj, _perm, _callback, _client_data)
        return ret

    def IsSecured(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocIsSecured(self.obj)
        return ret

    def SetSecurityHandler(self, _handler: PdfSecurityHandler) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocSetSecurityHandler(self.obj, _handler.obj if _handler else None)
        return ret

    def GetSecurityHandler(self) -> PdfSecurityHandler: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetSecurityHandler(self.obj)
        if ret:
            return PdfSecurityHandler(ret)
        else:
            return None

    def GetNumPages(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetNumPages(self.obj)
        return ret

    def AcquirePage(self, _page_num: int) -> PdfPage: 
        global PdfixLib
        ret = PdfixLib.PdfDocAcquirePage(self.obj, _page_num)
        if ret:
            return PdfPage(ret)
        else:
            return None

    def CreatePage(self, _index: int, _media_box: PdfRect) -> PdfPage: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreatePage(self.obj, _index, _media_box.GetIntStruct() if _media_box else None)
        if ret:
            return PdfPage(ret)
        else:
            return None

    def DeletePages(self, _index_from: int, _index_to: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocDeletePages(self.obj, _index_from, _index_to)
        return ret

    def InsertPages(self, _index: int, _doc: PdfDoc, _index_from: int, _index_to: int, _insert_flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocInsertPages(self.obj, _index, _doc.obj if _doc else None, _index_from, _index_to, _insert_flags)
        return ret

    def MovePage(self, _index_to: int, _index_from: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocMovePage(self.obj, _index_to, _index_from)
        return ret

    def GetNumDocumentJavaScripts(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetNumDocumentJavaScripts(self.obj)
        return ret

    def GetDocumentJavaScript(self, _index: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfDocGetDocumentJavaScript(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfDocGetDocumentJavaScript(self.obj, _index, _buffer, _len)
        return _buffer.value

    def GetDocumentJavaScriptName(self, _index: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfDocGetDocumentJavaScriptName(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfDocGetDocumentJavaScriptName(self.obj, _index, _buffer, _len)
        return _buffer.value

    def GetNumCalculatedFormFields(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetNumCalculatedFormFields(self.obj)
        return ret

    def GetCalculatedFormField(self, _index: int) -> PdfFormField: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetCalculatedFormField(self.obj, _index)
        if ret:
            return PdfFormField(ret)
        else:
            return None

    def GetNumFormFields(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetNumFormFields(self.obj)
        return ret

    def GetFormField(self, _index: int) -> PdfFormField: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetFormField(self.obj, _index)
        if ret:
            return PdfFormField(ret)
        else:
            return None

    def GetFormFieldByName(self, _buffer) -> PdfFormField: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetFormFieldByName(self.obj, _buffer)
        if ret:
            return PdfFormField(ret)
        else:
            return None

    def GetInfo(self, _key) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfDocGetInfo(self.obj, _key, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfDocGetInfo(self.obj, _key, _buffer, _len)
        return _buffer.value

    def SetInfo(self, _key, _info) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocSetInfo(self.obj, _key, _info)
        return ret

    def GetBookmarkRoot(self) -> PdfBookmark: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetBookmarkRoot(self.obj)
        if ret:
            return PdfBookmark(ret)
        else:
            return None

    def CreateBookmarkRoot(self) -> PdfBookmark: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateBookmarkRoot(self.obj)
        if ret:
            return PdfBookmark(ret)
        else:
            return None

    def ApplyRedaction(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocApplyRedaction(self.obj)
        return ret

    def GetNumAlternates(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetNumAlternates(self.obj)
        return ret

    def AcquireAlternate(self, _index: int) -> PdfAlternate: 
        global PdfixLib
        ret = PdfixLib.PdfDocAcquireAlternate(self.obj, _index)
        if ret:
            return PdfAlternate(ret)
        else:
            return None

    def AddTags(self, _tag_params: PdfTagsParams) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocAddTags(self.obj, _tag_params.GetIntStruct() if _tag_params else None)
        return ret

    def RemoveTags(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocRemoveTags(self.obj)
        return ret

    def GetTemplate(self) -> PdfDocTemplate: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetTemplate(self.obj)
        if ret:
            return PdfDocTemplate(ret)
        else:
            return None

    def GetMetadata(self) -> PdsStream: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetMetadata(self.obj)
        if ret:
            return PdsStream(ret)
        else:
            return None

    def GetLang(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfDocGetLang(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfDocGetLang(self.obj, _buffer, _len)
        return _buffer.value

    def SetLang(self, _lang) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocSetLang(self.obj, _lang)
        return ret

    def ReplaceFont(self, _font: PdfFont, _face_name) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocReplaceFont(self.obj, _font.obj if _font else None, _face_name)
        return ret

    def EmbedFont(self, _font: PdfFont, _subset: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocEmbedFont(self.obj, _font.obj if _font else None, _subset)
        return ret

    def EmbedFonts(self, _subset: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocEmbedFonts(self.obj, _subset)
        return ret

    def GetTrailerObject(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetTrailerObject(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def GetRootObject(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetRootObject(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def GetInfoObject(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetInfoObject(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def CreateDictObject(self, _indirect: bool) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateDictObject(self.obj, _indirect)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def CreateArrayObject(self, _indirect: bool) -> PdsArray: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateArrayObject(self.obj, _indirect)
        if ret:
            return PdsArray(ret)
        else:
            return None

    def CreateBooleanObject(self, _indirect: bool, _value: bool) -> PdsBoolean: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateBooleanObject(self.obj, _indirect, _value)
        if ret:
            return PdsBoolean(ret)
        else:
            return None

    def CreateNameObject(self, _indirect: bool, _value) -> PdsName: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateNameObject(self.obj, _indirect, _value)
        if ret:
            return PdsName(ret)
        else:
            return None

    def CreateStringObject(self, _indirect: bool, _value, _hex: bool) -> PdsString: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateStringObject(self.obj, _indirect, _value, _hex)
        if ret:
            return PdsString(ret)
        else:
            return None

    def CreateIntObject(self, _indirect: bool, _value: int) -> PdsNumber: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateIntObject(self.obj, _indirect, _value)
        if ret:
            return PdsNumber(ret)
        else:
            return None

    def CreateNumberObject(self, _indirect: bool, _value: float) -> PdsNumber: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateNumberObject(self.obj, _indirect, _value)
        if ret:
            return PdsNumber(ret)
        else:
            return None

    def CreateStreamObject(self, _indirect: bool, _dict: PdsDictionary, _buffer, _size: int) -> PdsStream: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateStreamObject(self.obj, _indirect, _dict.obj if _dict else None, _buffer, _size)
        if ret:
            return PdsStream(ret)
        else:
            return None

    def CreateXObjectFromImage(self, _image_data: PsStream, _format: int, _page_index: int) -> PdsStream: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateXObjectFromImage(self.obj, _image_data.obj if _image_data else None, _format, _page_index)
        if ret:
            return PdsStream(ret)
        else:
            return None

    def CreateXObjectFromPage(self, _page: PdfPage) -> PdsStream: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateXObjectFromPage(self.obj, _page.obj if _page else None)
        if ret:
            return PdsStream(ret)
        else:
            return None

    def GetObjectById(self, _obj_id: int) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetObjectById(self.obj, _obj_id)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def CreateStructTree(self) -> PdsStructTree: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateStructTree(self.obj)
        if ret:
            return PdsStructTree(ret)
        else:
            return None

    def GetStructTree(self) -> PdsStructTree: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetStructTree(self.obj)
        if ret:
            return PdsStructTree(ret)
        else:
            return None

    def RemoveStructTree(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocRemoveStructTree(self.obj)
        return ret

    def RemoveBookmarks(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocRemoveBookmarks(self.obj)
        return ret

    def CreateBookmarks(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateBookmarks(self.obj)
        return ret

    def AddFontMissingUnicode(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocAddFontMissingUnicode(self.obj)
        return ret

    def GetNameTree(self, _name, _create: bool) -> PdfNameTree: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetNameTree(self.obj, _name, _create)
        if ret:
            return PdfNameTree(ret)
        else:
            return None

    def RemoveNameTree(self, _name) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocRemoveNameTree(self.obj, _name)
        return ret

    def GetPageNumFromObject(self, _page_dict: PdsObject) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetPageNumFromObject(self.obj, _page_dict.obj if _page_dict else None)
        return ret

    def GetAnnotFromObject(self, _annot_dict: PdsObject) -> PdfAnnot: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetAnnotFromObject(self.obj, _annot_dict.obj if _annot_dict else None)
        if ret:
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotText:
                return PdfTextAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLink:
                return PdfLinkAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFreeText:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquare:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCircle:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolygon:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolyLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotHighlight:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotUnderline:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquiggly:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStrikeOut:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStamp:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCaret:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotInk:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPopup:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFileAttachment:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSound:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotMovie:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWidget:
                return PdfWidgetAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotScreen:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPrinterMark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotTrapNet:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWatermark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnot3D:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotRedact:
                return PdfAnnot(ret)
            return PdfAnnot(ret)
        else:
            return None

    def GetBookmarkFromObject(self, _bookmark_obj: PdsObject) -> PdfBookmark: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetBookmarkFromObject(self.obj, _bookmark_obj.obj if _bookmark_obj else None)
        if ret:
            return PdfBookmark(ret)
        else:
            return None

    def GetActionFromObject(self, _action_obj: PdsObject) -> PdfAction: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetActionFromObject(self.obj, _action_obj.obj if _action_obj else None)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def GetActionFromViewDest(self, _dest: PdfViewDestination) -> PdfAction: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetActionFromViewDest(self.obj, _dest.obj if _dest else None)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def GetViewDestinationFromObject(self, _dest_obj: PdsObject) -> PdfViewDestination: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetViewDestinationFromObject(self.obj, _dest_obj.obj if _dest_obj else None)
        if ret:
            return PdfViewDestination(ret)
        else:
            return None

    def CreateViewDestination(self, _page_num: int, _fit_type: int, _rect: PdfRect, _zoom: float) -> PdfViewDestination: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateViewDestination(self.obj, _page_num, _fit_type, _rect.GetIntStruct() if _rect else None, _zoom)
        if ret:
            return PdfViewDestination(ret)
        else:
            return None

    def CreateFormFromObject(self, _stream: PdsStream, _matrix: PdfMatrix) -> PdsForm: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateFormFromObject(self.obj, _stream.obj if _stream else None, _matrix.GetIntStruct() if _matrix else None)
        if ret:
            return PdsForm(ret)
        else:
            return None

    def CreateAction(self, _type: int) -> PdfAction: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateAction(self.obj, _type)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def CreateContent(self) -> PdsContent: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateContent(self.obj)
        if ret:
            return PdsContent(ret)
        else:
            return None

    def CreateColorSpace(self, _cs_family: int) -> PdfColorSpace: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateColorSpace(self.obj, _cs_family)
        if ret:
            return PdfColorSpace(ret)
        else:
            return None

    def CreateFont(self, _sys_font: PsSysFont, _charset: int, _flags: int) -> PdfFont: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateFont(self.obj, _sys_font.obj if _sys_font else None, _charset, _flags)
        if ret:
            return PdfFont(ret)
        else:
            return None

    def CreateUndo(self, _title, _client_data: int) -> PdfDocUndo: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateUndo(self.obj, _title, _client_data)
        if ret:
            return PdfDocUndo(ret)
        else:
            return None

    def GetNumUndos(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetNumUndos(self.obj)
        return ret

    def GetUndo(self, _index: int) -> PdfDocUndo: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetUndo(self.obj, _index)
        if ret:
            return PdfDocUndo(ret)
        else:
            return None

    def ClearUndos(self, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocClearUndos(self.obj, _index)
        return ret

    def GetNumRedos(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetNumRedos(self.obj)
        return ret

    def GetRedo(self, _index: int) -> PdfDocUndo: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetRedo(self.obj, _index)
        if ret:
            return PdfDocUndo(ret)
        else:
            return None

    def ClearRedos(self, _count: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocClearRedos(self.obj, _count)
        return ret

    def GetFlags(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetFlags(self.obj)
        return ret

    def SetFlags(self, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocSetFlags(self.obj, _flags)
        return ret

    def ClearFlags(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocClearFlags(self.obj)
        return ret

    def GetUserPermissions(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetUserPermissions(self.obj)
        return ret

    def GetVersion(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetVersion(self.obj)
        return ret

    def SetVersion(self, _version: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocSetVersion(self.obj, _version)
        return ret

    def GetPdfStandard(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetPdfStandard(self.obj)
        return ret

    def SetPdfStandard(self, _flags: int, _part) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocSetPdfStandard(self.obj, _flags, _part)
        return ret

    def GetPath(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfDocGetPath(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfDocGetPath(self.obj, _path, _len)
        return _buffer.value

    def SetPath(self, _path) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocSetPath(self.obj, _path)
        return ret

    def CreateHtmlConversion(self) -> PdfHtmlConversion: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateHtmlConversion(self.obj)
        if ret:
            return PdfHtmlConversion(ret)
        else:
            return None

    def CreateJsonConversion(self) -> PdfJsonConversion: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateJsonConversion(self.obj)
        if ret:
            return PdfJsonConversion(ret)
        else:
            return None

    def CreateTiffConversion(self) -> PdfTiffConversion: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateTiffConversion(self.obj)
        if ret:
            return PdfTiffConversion(ret)
        else:
            return None

    def GetCommand(self) -> PsCommand: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetCommand(self.obj)
        if ret:
            return PsCommand(ret)
        else:
            return None

    def EnumFonts(self, _flags: int, _proc, _client_data: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocEnumFonts(self.obj, _flags, _proc, _client_data)
        return ret

    def EnumBookmarks(self, _bmk: PdfBookmark, _flags: int, _proc, _client_data: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocEnumBookmarks(self.obj, _bmk.obj if _bmk else None, _flags, _proc, _client_data)
        return ret

    def EnumAnnots(self, _page_num: int, _flags: int, _proc, _client_data: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocEnumAnnots(self.obj, _page_num, _flags, _proc, _client_data)
        return ret

    def EnumPageObjects(self, _content: PdsContent, _object: PdsPageObject, _flags: int, _proc, _client_data: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocEnumPageObjects(self.obj, _content.obj if _content else None, _object.obj if _object else None, _flags, _proc, _client_data)
        return ret

    def EnumStructTree(self, _structElem: PdsStructElement, _flags: int, _proc, _client_data: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocEnumStructTree(self.obj, _structElem.obj if _structElem else None, _flags, _proc, _client_data)
        return ret

    def GetProgressControl(self) -> PsProgressControl: 
        global PdfixLib
        ret = PdfixLib.PdfDocGetProgressControl(self.obj)
        if ret:
            return PsProgressControl(ret)
        else:
            return None

    def CreateFileSpec(self, _name, _desc, _af_relationship, _subtype, _buffer, _size: int) -> PdsFileSpec: 
        global PdfixLib
        ret = PdfixLib.PdfDocCreateFileSpec(self.obj, _name, _desc, _af_relationship, _subtype, _buffer, _size)
        if ret:
            return PdsFileSpec(ret)
        else:
            return None

class PdsFileSpec(_PdfixBase):
    def __init__(self, _obj):
        super(PdsFileSpec, self).__init__(_obj)

    def GetDictionary(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdsFileSpecGetDictionary(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def GetFileName(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsFileSpecGetFileName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsFileSpecGetFileName(self.obj, _buffer, _len)
        return _buffer.value

    def SetFileName(self, _buffer) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsFileSpecSetFileName(self.obj, _buffer)
        return ret

    def GetFileStm(self) -> PdsStream: 
        global PdfixLib
        ret = PdfixLib.PdsFileSpecGetFileStm(self.obj)
        if ret:
            return PdsStream(ret)
        else:
            return None

class PdfDocTemplate(_PdfixBase):
    def __init__(self, _obj):
        super(PdfDocTemplate, self).__init__(_obj)

    def Update(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateUpdate(self.obj)
        return ret

    def LoadFromStream(self, _stream: PsStream, _format: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateLoadFromStream(self.obj, _stream.obj if _stream else None, _format)
        return ret

    def SaveToStream(self, _stream: PsStream, _format: int, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateSaveToStream(self.obj, _stream.obj if _stream else None, _format, _flags)
        return ret

    def SetDefaults(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateSetDefaults(self.obj)
        return ret

    def GetProperty(self, _name) -> float: 
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateGetProperty(self.obj, _name)
        return ret

    def SetProperty(self, _name, _value: float) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateSetProperty(self.obj, _name, _value)
        return ret

    def GetRegex(self, _name) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfDocTemplateGetRegex(self.obj, _name, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfDocTemplateGetRegex(self.obj, _name, _buffer, _len)
        return _buffer.value

    def SetRegex(self, _name, _pattern) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateSetRegex(self.obj, _name, _pattern)
        return ret

    def AddPage(self, _page_num: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateAddPage(self.obj, _page_num)
        return ret

    def GetPageTemplate(self, _page_num: int) -> PdfPageTemplate: 
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateGetPageTemplate(self.obj, _page_num)
        if ret:
            return PdfPageTemplate(ret)
        else:
            return None

    def GetNumNodes(self, _page_num: int, _path) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateGetNumNodes(self.obj, _page_num, _path)
        return ret

    def GetNodeBBox(self, _page_num: int, _path, _index: int) -> bool: 
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdfDocTemplateGetNodeBBox(self.obj, _page_num, _path, _index, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def GetVersionMajor(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateGetVersionMajor(self.obj)
        return ret

    def GetVersionMinor(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfDocTemplateGetVersionMinor(self.obj)
        return ret

class PdfPageTemplate(_PdfixBase):
    def __init__(self, _obj):
        super(PdfPageTemplate, self).__init__(_obj)

    def GetPageNum(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageTemplateGetPageNum(self.obj)
        return ret

    def GetLogicalRotate(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageTemplateGetLogicalRotate(self.obj)
        return ret

    def GetNumColumns(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageTemplateGetNumColumns(self.obj)
        return ret

    def GetHeaderBBox(self) -> bool: 
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdfPageTemplateGetHeaderBBox(self.obj, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def GetFooterBBox(self) -> bool: 
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdfPageTemplateGetFooterBBox(self.obj, _bbox)
        result.SetIntStruct(_bbox)
        return result

class PdfAlternate(_PdfixBase):
    def __init__(self, _obj):
        super(PdfAlternate, self).__init__(_obj)

    def GetSubtype(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfAlternateGetSubtype(self.obj)
        return ret

    def GetName(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfAlternateGetName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfAlternateGetName(self.obj, _buffer, _len)
        return _buffer.value

    def GetDescription(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfAlternateGetDescription(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfAlternateGetDescription(self.obj, _buffer, _len)
        return _buffer.value

    def GetFileName(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfAlternateGetFileName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfAlternateGetFileName(self.obj, _buffer, _len)
        return _buffer.value

    def SaveContent(self, _path) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfAlternateSaveContent(self.obj, _path)
        return ret

    def Release(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfAlternateRelease(self.obj)
        return ret

class PdfHtmlAlternate(PdfAlternate):
    def __init__(self, _obj):
        super(PdfHtmlAlternate, self).__init__(_obj)

    def SaveResource(self, _resource_name, _path) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfHtmlAlternateSaveResource(self.obj, _resource_name, _path)
        return ret

class PdfFont(_PdfixBase):
    def __init__(self, _obj):
        super(PdfFont, self).__init__(_obj)

    def GetFontName(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfFontGetFontName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFontGetFontName(self.obj, _buffer, _len)
        return _buffer.value

    def GetFaceName(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfFontGetFaceName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFontGetFaceName(self.obj, _buffer, _len)
        return _buffer.value

    def GetFontState(self): 
        global PdfixLib
        result = PdfFontState()
        _font_state = result.GetIntStruct()
        PdfixLib.PdfFontGetFontState(self.obj, _font_state)
        result.SetIntStruct(_font_state)
        return result

    def GetSystemFontName(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfFontGetSystemFontName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFontGetSystemFontName(self.obj, _buffer, _len)
        return _buffer.value

    def GetSystemFontCharset(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfFontGetSystemFontCharset(self.obj)
        return ret

    def GetSystemFontBold(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfFontGetSystemFontBold(self.obj)
        return ret

    def GetSystemFontItalic(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfFontGetSystemFontItalic(self.obj)
        return ret

    def SaveToStream(self, _stream: PsStream, _format: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfFontSaveToStream(self.obj, _stream.obj if _stream else None, _format)
        return ret

    def GetEmbedded(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfFontGetEmbedded(self.obj)
        return ret

    def GetUnicodeFromCharcode(self, _charcode: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfFontGetUnicodeFromCharcode(self.obj, _charcode, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFontGetUnicodeFromCharcode(self.obj, _charcode, _buffer, _len)
        return _buffer.value

    def SetUnicodeForCharcode(self, _charcode: int, _buffer) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfFontSetUnicodeForCharcode(self.obj, _charcode, _buffer)
        return ret

    def GetObject(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdfFontGetObject(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

class PdfFormField(_PdfixBase):
    def __init__(self, _obj):
        super(PdfFormField, self).__init__(_obj)

    def GetType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetType(self.obj)
        return ret

    def GetFlags(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetFlags(self.obj)
        return ret

    def SetFlags(self, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfFormFieldSetFlags(self.obj, _flags)
        return ret

    def GetValue(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetValue(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetValue(self.obj, _buffer, _len)
        return _buffer.value

    def SetValue(self, _value) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfFormFieldSetValue(self.obj, _value)
        return ret

    def GetDefaultValue(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetDefaultValue(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetDefaultValue(self.obj, _buffer, _len)
        return _buffer.value

    def GetFullName(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetFullName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetFullName(self.obj, _buffer, _len)
        return _buffer.value

    def GetTooltip(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetTooltip(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetTooltip(self.obj, _buffer, _len)
        return _buffer.value

    def GetNumOptions(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetNumOptions(self.obj)
        return ret

    def GetOptionValue(self, _index: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetOptionValue(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetOptionValue(self.obj, _index, _buffer, _len)
        return _buffer.value

    def GetOptionCaption(self, _index: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetOptionCaption(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetOptionCaption(self.obj, _index, _buffer, _len)
        return _buffer.value

    def GetAction(self) -> PdfAction: 
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetAction(self.obj)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def GetAAction(self, _event: int) -> PdfAction: 
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetAAction(self.obj, _event)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def GetMaxLength(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetMaxLength(self.obj)
        return ret

    def GetWidgetExportValue(self, _annot: PdfAnnot) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetWidgetExportValue(self.obj, _annot, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetWidgetExportValue(self.obj, _annot, _buffer, _len)
        return _buffer.value

    def GetObject(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetObject(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def GetNumExportValues(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfFormFieldGetNumExportValues(self.obj)
        return ret

    def GetExportValue(self, _index: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfFormFieldGetExportValue(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfFormFieldGetExportValue(self.obj, _index, _buffer, _len)
        return _buffer.value

    def NotifyWillChange(self, _key): 
        global PdfixLib
        ret = PdfixLib.PdfFormFieldNotifyWillChange(self.obj, _key)
        return ret

    def NotifyDidChange(self, _key, _err: int): 
        global PdfixLib
        ret = PdfixLib.PdfFormFieldNotifyDidChange(self.obj, _key, _err)
        return ret

class PdfPage(_PdfixBase):
    def __init__(self, _obj):
        super(PdfPage, self).__init__(_obj)

    def Release(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageRelease(self.obj)
        return ret

    def GetRefNum(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetRefNum(self.obj)
        return ret

    def GetCropBox(self): 
        global PdfixLib
        result = PdfRect()
        _crop_box = result.GetIntStruct()
        PdfixLib.PdfPageGetCropBox(self.obj, _crop_box)
        result.SetIntStruct(_crop_box)
        return result

    def GetMediaBox(self): 
        global PdfixLib
        result = PdfRect()
        _media_box = result.GetIntStruct()
        PdfixLib.PdfPageGetMediaBox(self.obj, _media_box)
        result.SetIntStruct(_media_box)
        return result

    def GetRotate(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetRotate(self.obj)
        return ret

    def SetRotate(self, _rotate: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfPageSetRotate(self.obj, _rotate)
        return ret

    def GetLogicalRotate(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetLogicalRotate(self.obj)
        return ret

    def GetDefaultMatrix(self): 
        global PdfixLib
        result = PdfMatrix()
        _matrix = result.GetIntStruct()
        PdfixLib.PdfPageGetDefaultMatrix(self.obj, _matrix)
        result.SetIntStruct(_matrix)
        return result

    def GetTemplateMatrix(self): 
        global PdfixLib
        result = PdfMatrix()
        _matrix = result.GetIntStruct()
        PdfixLib.PdfPageGetTemplateMatrix(self.obj, _matrix)
        result.SetIntStruct(_matrix)
        return result

    def GetNumber(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetNumber(self.obj)
        return ret

    def AcquirePageMap(self) -> PdePageMap: 
        global PdfixLib
        ret = PdfixLib.PdfPageAcquirePageMap(self.obj)
        if ret:
            return PdePageMap(ret)
        else:
            return None

    def AcquirePageView(self, _zoom: float, _rotate: int) -> PdfPageView: 
        global PdfixLib
        ret = PdfixLib.PdfPageAcquirePageView(self.obj, _zoom, _rotate)
        if ret:
            return PdfPageView(ret)
        else:
            return None

    def GetNumAnnots(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetNumAnnots(self.obj)
        return ret

    def GetAnnot(self, _index: int) -> PdfAnnot: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetAnnot(self.obj, _index)
        if ret:
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotText:
                return PdfTextAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLink:
                return PdfLinkAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFreeText:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquare:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCircle:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolygon:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolyLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotHighlight:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotUnderline:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquiggly:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStrikeOut:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStamp:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCaret:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotInk:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPopup:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFileAttachment:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSound:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotMovie:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWidget:
                return PdfWidgetAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotScreen:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPrinterMark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotTrapNet:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWatermark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnot3D:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotRedact:
                return PdfAnnot(ret)
            return PdfAnnot(ret)
        else:
            return None

    def RemoveAnnot(self, _index: int, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfPageRemoveAnnot(self.obj, _index, _flags)
        return ret

    def AddAnnot(self, _index: int, _annot: PdfAnnot) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfPageAddAnnot(self.obj, _index, _annot.obj if _annot else None)
        return ret

    def CreateAnnot(self, _subtype: int, _rect: PdfRect) -> PdfAnnot: 
        global PdfixLib
        ret = PdfixLib.PdfPageCreateAnnot(self.obj, _subtype, _rect.GetIntStruct() if _rect else None)
        if ret:
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotText:
                return PdfTextAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLink:
                return PdfLinkAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFreeText:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquare:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCircle:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolygon:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolyLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotHighlight:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotUnderline:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquiggly:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStrikeOut:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStamp:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCaret:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotInk:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPopup:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFileAttachment:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSound:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotMovie:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWidget:
                return PdfWidgetAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotScreen:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPrinterMark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotTrapNet:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWatermark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnot3D:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotRedact:
                return PdfAnnot(ret)
            return PdfAnnot(ret)
        else:
            return None

    def GetNumAnnotsAtPoint(self, _point: PdfPoint) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetNumAnnotsAtPoint(self.obj, _point.GetIntStruct() if _point else None)
        return ret

    def GetAnnotAtPoint(self, _point: PdfPoint, _index: int) -> PdfAnnot: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetAnnotAtPoint(self.obj, _point.GetIntStruct() if _point else None, _index)
        if ret:
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotText:
                return PdfTextAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLink:
                return PdfLinkAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFreeText:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquare:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCircle:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolygon:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolyLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotHighlight:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotUnderline:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquiggly:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStrikeOut:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStamp:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCaret:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotInk:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPopup:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFileAttachment:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSound:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotMovie:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWidget:
                return PdfWidgetAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotScreen:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPrinterMark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotTrapNet:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWatermark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnot3D:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotRedact:
                return PdfAnnot(ret)
            return PdfAnnot(ret)
        else:
            return None

    def GetNumAnnotsAtRect(self, _rect: PdfRect) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetNumAnnotsAtRect(self.obj, _rect.GetIntStruct() if _rect else None)
        return ret

    def GetAnnotAtRect(self, _rect: PdfRect, _index: int) -> PdfAnnot: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetAnnotAtRect(self.obj, _rect.GetIntStruct() if _rect else None, _index)
        if ret:
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotText:
                return PdfTextAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLink:
                return PdfLinkAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFreeText:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquare:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCircle:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolygon:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPolyLine:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotHighlight:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotUnderline:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSquiggly:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStrikeOut:
                return PdfTextMarkupAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotStamp:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotCaret:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotInk:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPopup:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotFileAttachment:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotSound:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotMovie:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWidget:
                return PdfWidgetAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotScreen:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotPrinterMark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotTrapNet:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotWatermark:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnot3D:
                return PdfAnnot(ret)
            if PdfixLib.PdfAnnotGetSubtype(ret) == kAnnotRedact:
                return PdfAnnot(ret)
            return PdfAnnot(ret)
        else:
            return None

    def DrawContent(self, _params: PdfPageRenderParams) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfPageDrawContent(self.obj, _params.GetIntStruct() if _params else None)
        return ret

    def GetContent(self) -> PdsContent: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetContent(self.obj)
        if ret:
            return PdsContent(ret)
        else:
            return None

    def GetResources(self, _res_type, _create: bool) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetResources(self.obj, _res_type, _create)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def GetObject(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetObject(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def FlattenFormXObjects(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfPageFlattenFormXObjects(self.obj)
        return ret

    def CloneFormXObjects(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfPageCloneFormXObjects(self.obj)
        return ret

    def FlattenAnnot(self, _annot: PdfAnnot) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfPageFlattenAnnot(self.obj, _annot.obj if _annot else None)
        return ret

    def GetContentFlags(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetContentFlags(self.obj)
        return ret

    def SetContent(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfPageSetContent(self.obj)
        return ret

    def GetDoc(self) -> PdfDoc: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetDoc(self.obj)
        if ret:
            return PdfDoc(ret)
        else:
            return None

    def AcquireWordList(self, _alg: int, _flags: int) -> PdeWordList: 
        global PdfixLib
        ret = PdfixLib.PdfPageAcquireWordList(self.obj, _alg, _flags)
        if ret:
            return PdeWordList(ret)
        else:
            return None

    def GetFlags(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageGetFlags(self.obj)
        return ret

    def SetFlags(self, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfPageSetFlags(self.obj, _flags)
        return ret

    def ClearFlags(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfPageClearFlags(self.obj)
        return ret

    def CreateFormFromObject(self, _stream: PdsStream) -> PdsForm: 
        global PdfixLib
        ret = PdfixLib.PdfPageCreateFormFromObject(self.obj, _stream.obj if _stream else None)
        if ret:
            return PdsForm(ret)
        else:
            return None

class PdePageMap(_PdfixBase):
    def __init__(self, _obj):
        super(PdePageMap, self).__init__(_obj)

    def Release(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdePageMapRelease(self.obj)
        return ret

    def GetElement(self) -> PdeElement: 
        global PdfixLib
        ret = PdfixLib.PdePageMapGetElement(self.obj)
        if ret:
            if PdfixLib.PdeElementGetType(ret) == kPdeText:
                return PdeText(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTextLine:
                return PdeTextLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeWord:
                return PdeWord(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeImage:
                return PdeImage(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeContainer:
                return PdeContainer(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeList:
                return PdeList(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeLine:
                return PdeLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeRect:
                return PdeRect(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeHeader:
                return PdeHeader(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFooter:
                return PdeFooter(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeArtifact:
                return PdeArtifact(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTable:
                return PdeTable(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeCell:
                return PdeCell(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFormField:
                return PdeFormField(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeToc:
                return PdeToc(ret)
            return PdeElement(ret)
        else:
            return None

    def GetWhitespace(self, _params: PdfWhitespaceParams, _index: int) -> bool: 
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdePageMapGetWhitespace(self.obj, _params.GetIntStruct(), _index, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def GetBBox(self): 
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdePageMapGetBBox(self.obj, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def HasElements(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdePageMapHasElements(self.obj)
        return ret

    def CreateElements(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdePageMapCreateElements(self.obj)
        return ret

    def RemoveElements(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdePageMapRemoveElements(self.obj)
        return ret

    def CreateElement(self, _type: int, _parent: PdeElement) -> PdeElement: 
        global PdfixLib
        ret = PdfixLib.PdePageMapCreateElement(self.obj, _type, _parent.obj if _parent else None)
        if ret:
            if PdfixLib.PdeElementGetType(ret) == kPdeText:
                return PdeText(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTextLine:
                return PdeTextLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeWord:
                return PdeWord(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeImage:
                return PdeImage(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeContainer:
                return PdeContainer(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeList:
                return PdeList(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeLine:
                return PdeLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeRect:
                return PdeRect(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeHeader:
                return PdeHeader(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFooter:
                return PdeFooter(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeArtifact:
                return PdeArtifact(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTable:
                return PdeTable(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeCell:
                return PdeCell(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFormField:
                return PdeFormField(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeToc:
                return PdeToc(ret)
            return PdeElement(ret)
        else:
            return None

    def AddTags(self, _element: PdsStructElement, _sibling: bool, _tag_params: PdfTagsParams) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdePageMapAddTags(self.obj, _element.obj if _element else None, _sibling, _tag_params.GetIntStruct() if _tag_params else None)
        return ret

    def GetPage(self) -> PdfPage: 
        global PdfixLib
        ret = PdfixLib.PdePageMapGetPage(self.obj)
        if ret:
            return PdfPage(ret)
        else:
            return None

    def GetNumArtifacts(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdePageMapGetNumArtifacts(self.obj)
        return ret

    def GetArtifact(self, _index: int) -> PdeElement: 
        global PdfixLib
        ret = PdfixLib.PdePageMapGetArtifact(self.obj, _index)
        if ret:
            if PdfixLib.PdeElementGetType(ret) == kPdeText:
                return PdeText(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTextLine:
                return PdeTextLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeWord:
                return PdeWord(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeImage:
                return PdeImage(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeContainer:
                return PdeContainer(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeList:
                return PdeList(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeLine:
                return PdeLine(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeRect:
                return PdeRect(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeHeader:
                return PdeHeader(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFooter:
                return PdeFooter(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeArtifact:
                return PdeArtifact(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeTable:
                return PdeTable(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeCell:
                return PdeCell(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeFormField:
                return PdeFormField(ret)
            if PdfixLib.PdeElementGetType(ret) == kPdeToc:
                return PdeToc(ret)
            return PdeElement(ret)
        else:
            return None

class PdfPageView(_PdfixBase):
    def __init__(self, _obj):
        super(PdfPageView, self).__init__(_obj)

    def Release(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageViewRelease(self.obj)
        return ret

    def GetDeviceWidth(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageViewGetDeviceWidth(self.obj)
        return ret

    def GetDeviceHeight(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfPageViewGetDeviceHeight(self.obj)
        return ret

    def GetDeviceMatrix(self): 
        global PdfixLib
        result = PdfMatrix()
        _matrix = result.GetIntStruct()
        PdfixLib.PdfPageViewGetDeviceMatrix(self.obj, _matrix)
        result.SetIntStruct(_matrix)
        return result

    def RectToDevice(self, _rect: PdfRect): 
        global PdfixLib
        result = PdfDevRect()
        _dev_rect = result.GetIntStruct()
        PdfixLib.PdfPageViewRectToDevice(self.obj, _rect.GetIntStruct(), _dev_rect)
        result.SetIntStruct(_dev_rect)
        return result

    def PointToDevice(self, _point: PdfPoint): 
        global PdfixLib
        result = PdfDevPoint()
        _dev_point = result.GetIntStruct()
        PdfixLib.PdfPageViewPointToDevice(self.obj, _point.GetIntStruct(), _dev_point)
        result.SetIntStruct(_dev_point)
        return result

    def RectToPage(self, _dev_rect: PdfDevRect): 
        global PdfixLib
        result = PdfRect()
        _rect = result.GetIntStruct()
        PdfixLib.PdfPageViewRectToPage(self.obj, _dev_rect.GetIntStruct(), _rect)
        result.SetIntStruct(_rect)
        return result

    def PointToPage(self, _dev_point: PdfDevPoint): 
        global PdfixLib
        result = PdfPoint()
        _point = result.GetIntStruct()
        PdfixLib.PdfPageViewPointToPage(self.obj, _dev_point.GetIntStruct(), _point)
        result.SetIntStruct(_point)
        return result

class PdfBookmark(_PdfixBase):
    def __init__(self, _obj):
        super(PdfBookmark, self).__init__(_obj)

    def GetTitle(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfBookmarkGetTitle(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfBookmarkGetTitle(self.obj, _buffer, _len)
        return _buffer.value

    def SetTitle(self, _title): 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkSetTitle(self.obj, _title)
        return ret

    def GetAppearance(self) -> bool: 
        global PdfixLib
        result = PdfBookmarkAppearance()
        _appearance = result.GetIntStruct()
        PdfixLib.PdfBookmarkGetAppearance(self.obj, _appearance)
        result.SetIntStruct(_appearance)
        return result

    def SetAppearance(self, _appearance: PdfBookmarkAppearance) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkSetAppearance(self.obj, _appearance.GetIntStruct() if _appearance else None)
        return ret

    def GetAction(self) -> PdfAction: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkGetAction(self.obj)
        if ret:
            return PdfAction(ret)
        else:
            return None

    def SetAction(self, _action: PdfAction) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkSetAction(self.obj, _action.obj if _action else None)
        return ret

    def GetNumChildren(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkGetNumChildren(self.obj)
        return ret

    def GetChild(self, _index: int) -> PdfBookmark: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkGetChild(self.obj, _index)
        if ret:
            return PdfBookmark(ret)
        else:
            return None

    def GetParent(self) -> PdfBookmark: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkGetParent(self.obj)
        if ret:
            return PdfBookmark(ret)
        else:
            return None

    def GetNext(self) -> PdfBookmark: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkGetNext(self.obj)
        if ret:
            return PdfBookmark(ret)
        else:
            return None

    def GetPrev(self) -> PdfBookmark: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkGetPrev(self.obj)
        if ret:
            return PdfBookmark(ret)
        else:
            return None

    def GetObject(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkGetObject(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def AddChild(self, _index: int, _bmk: PdfBookmark) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkAddChild(self.obj, _index, _bmk.obj if _bmk else None)
        return ret

    def AddNewChild(self, _index: int, _title) -> PdfBookmark: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkAddNewChild(self.obj, _index, _title)
        if ret:
            return PdfBookmark(ret)
        else:
            return None

    def IsValid(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkIsValid(self.obj)
        return ret

    def RemoveChild(self, _index: int) -> PdfBookmark: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkRemoveChild(self.obj, _index)
        if ret:
            return PdfBookmark(ret)
        else:
            return None

    def IsOpen(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkIsOpen(self.obj)
        return ret

    def SetOpen(self, _open: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfBookmarkSetOpen(self.obj, _open)
        return ret

class PdfNameTree(_PdfixBase):
    def __init__(self, _obj):
        super(PdfNameTree, self).__init__(_obj)

    def GetObject(self) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdfNameTreeGetObject(self.obj)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def Lookup(self, _name) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdfNameTreeLookup(self.obj, _name)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

class PsRegex(_PdfixBase):
    def __init__(self, _obj):
        super(PsRegex, self).__init__(_obj)

    def Destroy(self): 
        global PdfixLib
        ret = PdfixLib.PsRegexDestroy(self.obj)
        return ret

    def SetPattern(self, _pattern) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsRegexSetPattern(self.obj, _pattern)
        return ret

    def Search(self, _text, _position: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsRegexSearch(self.obj, _text, _position)
        return ret

    def GetText(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PsRegexGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PsRegexGetText(self.obj, _buffer, _len)
        return _buffer.value

    def GetPosition(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PsRegexGetPosition(self.obj)
        return ret

    def GetLength(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PsRegexGetLength(self.obj)
        return ret

    def GetNumMatches(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PsRegexGetNumMatches(self.obj)
        return ret

    def GetMatchText(self, _index: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PsRegexGetMatchText(self.obj, _index, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PsRegexGetMatchText(self.obj, _index, _buffer, _len)
        return _buffer.value

class PsStream(_PdfixBase):
    def __init__(self, _obj):
        super(PsStream, self).__init__(_obj)

    def Destroy(self): 
        global PdfixLib
        ret = PdfixLib.PsStreamDestroy(self.obj)
        return ret

    def IsEof(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsStreamIsEof(self.obj)
        return ret

    def GetSize(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PsStreamGetSize(self.obj)
        return ret

    def Read(self, _offset: int, _buffer, _size: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsStreamRead(self.obj, _offset, _buffer, _size)
        return ret

    def Write(self, _offset: int, _buffer, _size: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsStreamWrite(self.obj, _offset, _buffer, _size)
        return ret

    def GetPos(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PsStreamGetPos(self.obj)
        return ret

    def Flush(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsStreamFlush(self.obj)
        return ret

    def GetStream(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PsStreamGetStream(self.obj)
        return ret

    def GetType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PsStreamGetType(self.obj)
        return ret

class PsFileStream(PsStream):
    def __init__(self, _obj):
        super(PsFileStream, self).__init__(_obj)

class PsMemoryStream(PsStream):
    def __init__(self, _obj):
        super(PsMemoryStream, self).__init__(_obj)

    def Resize(self, _size: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsMemoryStreamResize(self.obj, _size)
        return ret

class PsCustomStream(PsStream):
    def __init__(self, _obj):
        super(PsCustomStream, self).__init__(_obj)

    def SetReadProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PsCustomStreamSetReadProc(self.obj, _proc)
        return ret

    def SetWriteProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PsCustomStreamSetWriteProc(self.obj, _proc)
        return ret

    def SetDestroyProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PsCustomStreamSetDestroyProc(self.obj, _proc)
        return ret

    def SetGetSizeProc(self, _proc): 
        global PdfixLib
        ret = PdfixLib.PsCustomStreamSetGetSizeProc(self.obj, _proc)
        return ret

class PdsStructElement(_PdfixBase):
    def __init__(self, _obj):
        super(PdsStructElement, self).__init__(_obj)

    def GetType(self, _mapped: bool) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetType(self.obj, _mapped, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetType(self.obj, _mapped, _buffer, _len)
        return _buffer.value

    def SetType(self, _type) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementSetType(self.obj, _type)
        return ret

    def GetActualText(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetActualText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetActualText(self.obj, _buffer, _len)
        return _buffer.value

    def SetActualText(self, _alt) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementSetActualText(self.obj, _alt)
        return ret

    def GetAlt(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetAlt(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetAlt(self.obj, _buffer, _len)
        return _buffer.value

    def SetAlt(self, _alt) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementSetAlt(self.obj, _alt)
        return ret

    def GetTitle(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetTitle(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetTitle(self.obj, _buffer, _len)
        return _buffer.value

    def SetTitle(self, _title) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementSetTitle(self.obj, _title)
        return ret

    def GetText(self, _max: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetText(self.obj, _max, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetText(self.obj, _max, _buffer, _len)
        return _buffer.value

    def GetAbbreviation(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetAbbreviation(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetAbbreviation(self.obj, _buffer, _len)
        return _buffer.value

    def GetNumPages(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetNumPages(self.obj)
        return ret

    def GetPageNumber(self, _index: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetPageNumber(self.obj, _index)
        return ret

    def GetBBox(self, _page_num: int): 
        global PdfixLib
        result = PdfRect()
        _bbox = result.GetIntStruct()
        PdfixLib.PdsStructElementGetBBox(self.obj, _page_num, _bbox)
        result.SetIntStruct(_bbox)
        return result

    def GetAttrObject(self, _index: int) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetAttrObject(self.obj, _index)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def AddAttrObj(self, _object: PdsObject) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementAddAttrObj(self.obj, _object.obj if _object else None)
        return ret

    def RemoveAttrObj(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementRemoveAttrObj(self.obj)
        return ret

    def GetObject(self) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetObject(self.obj)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def GetChildObject(self, _index: int) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetChildObject(self.obj, _index)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def GetChildType(self, _index: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetChildType(self.obj, _index)
        return ret

    def GetChildPageNumber(self, _index: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetChildPageNumber(self.obj, _index)
        return ret

    def GetChildMcid(self, _index: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetChildMcid(self.obj, _index)
        return ret

    def GetNumAttrObjects(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetNumAttrObjects(self.obj)
        return ret

    def GetNumChildren(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetNumChildren(self.obj)
        return ret

    def GetParentObject(self) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetParentObject(self.obj)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def GetId(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetId(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetId(self.obj, _buffer, _len)
        return _buffer.value

    def SetId(self, _id) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementSetId(self.obj, _id)
        return ret

    def GetLang(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsStructElementGetLang(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsStructElementGetLang(self.obj, _buffer, _len)
        return _buffer.value

    def SetLang(self, _alt) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementSetLang(self.obj, _alt)
        return ret

    def RemoveChild(self, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementRemoveChild(self.obj, _index)
        return ret

    def MoveChild(self, _index: int, _dest_element: PdsStructElement, _dest_index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementMoveChild(self.obj, _index, _dest_element.obj if _dest_element else None, _dest_index)
        return ret

    def AddChild(self, _element: PdsStructElement, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementAddChild(self.obj, _element.obj if _element else None, _index)
        return ret

    def AddNewChild(self, _type, _index: int) -> PdsStructElement: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementAddNewChild(self.obj, _type, _index)
        if ret:
            return PdsStructElement(ret)
        else:
            return None

    def AddPageObject(self, _object: PdsPageObject, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementAddPageObject(self.obj, _object.obj if _object else None, _index)
        return ret

    def AddAnnot(self, _annot: PdfAnnot, _index: int) -> PdsStructElement: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementAddAnnot(self.obj, _annot.obj if _annot else None, _index)
        if ret:
            return PdsStructElement(ret)
        else:
            return None

    def GetStructTree(self) -> PdsStructTree: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetStructTree(self.obj)
        if ret:
            return PdsStructTree(ret)
        else:
            return None

    def RecognizeTable(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementRecognizeTable(self.obj)
        return ret

    def GetNumRow(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetNumRow(self.obj)
        return ret

    def GetNumCol(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetNumCol(self.obj)
        return ret

    def GetCell(self, _row: int, _col: int) -> PdsStructElement: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetCell(self.obj, _row, _col)
        if ret:
            return PdsStructElement(ret)
        else:
            return None

    def GetCellParams(self, _row: int, _col: int) -> bool: 
        global PdfixLib
        result = PdfCellParams()
        _params = result.GetIntStruct()
        PdfixLib.PdsStructElementGetCellParams(self.obj, _row, _col, _params)
        result.SetIntStruct(_params)
        return result

    def GetCellElemParams(self, _cell: PdsStructElement) -> bool: 
        global PdfixLib
        result = PdfCellParams()
        _params = result.GetIntStruct()
        PdfixLib.PdsStructElementGetCellElemParams(self.obj, _cell.GetIntStruct(), _params)
        result.SetIntStruct(_params)
        return result

    def GetNumAssociatedHeaders(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetNumAssociatedHeaders(self.obj)
        return ret

    def GetAssociatedHeader(self, _index: int) -> PdsStructElement: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetAssociatedHeader(self.obj, _index)
        if ret:
            return PdsStructElement(ret)
        else:
            return None

    def AddAssociatedHeader(self, _index: int, _header: PdsStructElement, _create: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementAddAssociatedHeader(self.obj, _index, _header.obj if _header else None, _create)
        return ret

    def RemoveAssociatedHeader(self, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementRemoveAssociatedHeader(self.obj, _index)
        return ret

    def AddAssociatedFile(self, _file_spec: PdsFileSpec, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementAddAssociatedFile(self.obj, _file_spec.obj if _file_spec else None, _index)
        return ret

    def GetNumAssociatedFiles(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetNumAssociatedFiles(self.obj)
        return ret

    def GetAssociatedFile(self, _index: int) -> PdsFileSpec: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementGetAssociatedFile(self.obj, _index)
        if ret:
            return PdsFileSpec(ret)
        else:
            return None

    def ValidChild(self, _version: int, _child: PdsStructElement) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStructElementValidChild(self.obj, _version, _child.obj if _child else None)
        return ret

class PdsClassMap(_PdfixBase):
    def __init__(self, _obj):
        super(PdsClassMap, self).__init__(_obj)

    def GetAttrObject(self, _class_name, _index: int) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdsClassMapGetAttrObject(self.obj, _class_name, _index)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def GetNumAttrObjects(self, _class_name) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsClassMapGetNumAttrObjects(self.obj, _class_name)
        return ret

    def GetObject(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdsClassMapGetObject(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

class PdsRoleMap(_PdfixBase):
    def __init__(self, _obj):
        super(PdsRoleMap, self).__init__(_obj)

    def DoesMap(self, _src, _dst) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsRoleMapDoesMap(self.obj, _src, _dst)
        return ret

    def GetDirectMap(self, _type) -> str: 
        global PdfixLib
        _len = PdfixLib.PdsRoleMapGetDirectMap(self.obj, _type, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdsRoleMapGetDirectMap(self.obj, _type, _buffer, _len)
        return _buffer.value

    def GetObject(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdsRoleMapGetObject(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

class PdsStructTree(_PdfixBase):
    def __init__(self, _obj):
        super(PdsStructTree, self).__init__(_obj)

    def GetObject(self) -> PdsDictionary: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeGetObject(self.obj)
        if ret:
            return PdsDictionary(ret)
        else:
            return None

    def GetClassMap(self) -> PdsClassMap: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeGetClassMap(self.obj)
        if ret:
            return PdsClassMap(ret)
        else:
            return None

    def CreateClassMap(self) -> PdsClassMap: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeCreateClassMap(self.obj)
        if ret:
            return PdsClassMap(ret)
        else:
            return None

    def RemoveClassMap(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeRemoveClassMap(self.obj)
        return ret

    def GetChildObject(self, _index: int) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeGetChildObject(self.obj, _index)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def GetNumChildren(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeGetNumChildren(self.obj)
        return ret

    def GetRoleMap(self) -> PdsRoleMap: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeGetRoleMap(self.obj)
        if ret:
            return PdsRoleMap(ret)
        else:
            return None

    def CreateRoleMap(self) -> PdsRoleMap: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeCreateRoleMap(self.obj)
        if ret:
            return PdsRoleMap(ret)
        else:
            return None

    def RemoveRoleMap(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeRemoveRoleMap(self.obj)
        return ret

    def GetStructElementFromObject(self, _object: PdsObject) -> PdsStructElement: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeGetStructElementFromObject(self.obj, _object.obj if _object else None)
        if ret:
            return PdsStructElement(ret)
        else:
            return None

    def RemoveChild(self, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeRemoveChild(self.obj, _index)
        return ret

    def AddChild(self, _element: PdsStructElement, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeAddChild(self.obj, _element.obj if _element else None, _index)
        return ret

    def AddNewChild(self, _type, _index: int) -> PdsStructElement: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeAddNewChild(self.obj, _type, _index)
        if ret:
            return PdsStructElement(ret)
        else:
            return None

    def GetDoc(self) -> PdfDoc: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeGetDoc(self.obj)
        if ret:
            return PdfDoc(ret)
        else:
            return None

    def FixParentTree(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeFixParentTree(self.obj)
        return ret

    def FixIdTree(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdsStructTreeFixIdTree(self.obj)
        return ret

class PdfConversion(_PdfixBase):
    def __init__(self, _obj):
        super(PdfConversion, self).__init__(_obj)

    def Destroy(self): 
        global PdfixLib
        ret = PdfixLib.PdfConversionDestroy(self.obj)
        return ret

    def AddPage(self, _index: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfConversionAddPage(self.obj, _index)
        return ret

    def Save(self, _path) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfConversionSave(self.obj, _path)
        return ret

    def SaveToStream(self, _stream: PsStream) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfConversionSaveToStream(self.obj, _stream.obj if _stream else None)
        return ret

class PdfHtmlConversion(PdfConversion):
    def __init__(self, _obj):
        super(PdfHtmlConversion, self).__init__(_obj)

    def SetParams(self, _params: PdfHtmlParams) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfHtmlConversionSetParams(self.obj, _params.GetIntStruct() if _params else None)
        return ret

    def SaveCSS(self, _stream: PsStream) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfHtmlConversionSaveCSS(self.obj, _stream.obj if _stream else None)
        return ret

    def SaveJavaScript(self, _stream: PsStream) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfHtmlConversionSaveJavaScript(self.obj, _stream.obj if _stream else None)
        return ret

    def AddHtml(self, _stream: PsStream) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfHtmlConversionAddHtml(self.obj, _stream.obj if _stream else None)
        return ret

class PdfJsonConversion(PdfConversion):
    def __init__(self, _obj):
        super(PdfJsonConversion, self).__init__(_obj)

    def SetParams(self, _params: PdfJsonParams) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfJsonConversionSetParams(self.obj, _params.GetIntStruct() if _params else None)
        return ret

class PdfTiffConversion(PdfConversion):
    def __init__(self, _obj):
        super(PdfTiffConversion, self).__init__(_obj)

    def SetParams(self, _params: PdfTiffParams) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfTiffConversionSetParams(self.obj, _params.GetIntStruct() if _params else None)
        return ret

class PdfSelection(_PdfixBase):
    def __init__(self, _obj):
        super(PdfSelection, self).__init__(_obj)

    def EnumPageObjects(self, _proc, _data: int, _flags: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfSelectionEnumPageObjects(self.obj, _proc, _data, _flags)
        return ret

    def EnumPages(self, _proc, _data: int, _flags: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfSelectionEnumPages(self.obj, _proc, _data, _flags)
        return ret

    def EnumStructElements(self, _proc, _data: int, _flags: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfSelectionEnumStructElements(self.obj, _proc, _data, _flags)
        return ret

    def EnumAnnots(self, _proc, _data: int, _flags: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfSelectionEnumAnnots(self.obj, _proc, _data, _flags)
        return ret

    def EnumFonts(self, _proc, _data: int, _flags: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfSelectionEnumFonts(self.obj, _proc, _data, _flags)
        return ret

class PsEvent(_PdfixBase):
    def __init__(self, _obj):
        super(PsEvent, self).__init__(_obj)

    def GetType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PsEventGetType(self.obj)
        return ret

    def GetDoc(self) -> PdfDoc: 
        global PdfixLib
        ret = PdfixLib.PsEventGetDoc(self.obj)
        if ret:
            return PdfDoc(ret)
        else:
            return None

    def GetPage(self) -> PdfPage: 
        global PdfixLib
        ret = PdfixLib.PsEventGetPage(self.obj)
        if ret:
            return PdfPage(ret)
        else:
            return None

    def GetObject(self) -> PdsObject: 
        global PdfixLib
        ret = PdfixLib.PsEventGetObject(self.obj)
        if ret:
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsBoolean:
                return PdsBoolean(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsNumber:
                return PdsNumber(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsString:
                return PdsString(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsName:
                return PdsName(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsArray:
                return PdsArray(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsDictionary:
                return PdsDictionary(ret)
            if PdfixLib.PdsObjectGetObjectType(ret) == kPdsStream:
                return PdsStream(ret)
            return PdsObject(ret)
        else:
            return None

    def GetFormField(self) -> PdfFormField: 
        global PdfixLib
        ret = PdfixLib.PsEventGetFormField(self.obj)
        if ret:
            return PdfFormField(ret)
        else:
            return None

    def GetProgressControl(self) -> PsProgressControl: 
        global PdfixLib
        ret = PdfixLib.PsEventGetProgressControl(self.obj)
        if ret:
            return PsProgressControl(ret)
        else:
            return None

    def GetUndo(self) -> PdfDocUndo: 
        global PdfixLib
        ret = PdfixLib.PsEventGetUndo(self.obj)
        if ret:
            return PdfDocUndo(ret)
        else:
            return None

    def GetName(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PsEventGetName(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PsEventGetName(self.obj, _buffer, _len)
        return _buffer.value

    def GetIndex(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PsEventGetIndex(self.obj)
        return ret

class PsAuthorization(_PdfixBase):
    def __init__(self, _obj):
        super(PsAuthorization, self).__init__(_obj)

    def SaveToStream(self, _stream: PsStream, _format: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsAuthorizationSaveToStream(self.obj, _stream.obj if _stream else None, _format)
        return ret

    def IsAuthorized(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsAuthorizationIsAuthorized(self.obj)
        return ret

    def IsAuthorizedPlatform(self, _platform: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsAuthorizationIsAuthorizedPlatform(self.obj, _platform)
        return ret

    def IsAuthorizedOption(self, _option: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsAuthorizationIsAuthorizedOption(self.obj, _option)
        return ret

    def GetType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PsAuthorizationGetType(self.obj)
        return ret

class PsAccountAuthorization(PsAuthorization):
    def __init__(self, _obj):
        super(PsAccountAuthorization, self).__init__(_obj)

    def Authorize(self, _email, _serial_number) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsAccountAuthorizationAuthorize(self.obj, _email, _serial_number)
        return ret

    def Reset(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsAccountAuthorizationReset(self.obj)
        return ret

class PsStandardAuthorization(PsAuthorization):
    def __init__(self, _obj):
        super(PsStandardAuthorization, self).__init__(_obj)

    def Activate(self, _serial_number) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsStandardAuthorizationActivate(self.obj, _serial_number)
        return ret

    def CreateOfflineActivationFile(self, _serial_number, _activation_request_file) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsStandardAuthorizationCreateOfflineActivationFile(self.obj, _serial_number, _activation_request_file)
        return ret

    def ActivateOffline(self, _activation_file) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsStandardAuthorizationActivateOffline(self.obj, _activation_file)
        return ret

    def Deactivate(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsStandardAuthorizationDeactivate(self.obj)
        return ret

    def DeactivateOffline(self, _deactivation_request_file) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsStandardAuthorizationDeactivateOffline(self.obj, _deactivation_request_file)
        return ret

    def Update(self, _local: bool) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsStandardAuthorizationUpdate(self.obj, _local)
        return ret

    def UpdateOffline(self, _update_file) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsStandardAuthorizationUpdateOffline(self.obj, _update_file)
        return ret

    def Reset(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsStandardAuthorizationReset(self.obj)
        return ret

class PsCommand(_PdfixBase):
    def __init__(self, _obj):
        super(PsCommand, self).__init__(_obj)

    def LoadParamsFromStream(self, _params: PsStream, _format: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsCommandLoadParamsFromStream(self.obj, _params.obj if _params else None, _format)
        return ret

    def Reset(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsCommandReset(self.obj)
        return ret

    def SaveOutputToStream(self, _stream: PsStream, _format: int, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsCommandSaveOutputToStream(self.obj, _stream.obj if _stream else None, _format, _flags)
        return ret

    def SaveCommandsToStream(self, _type: int, _stream: PsStream, _format: int, _flags: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsCommandSaveCommandsToStream(self.obj, _type, _stream.obj if _stream else None, _format, _flags)
        return ret

    def SetSelection(self, _selection: PdfSelection) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsCommandSetSelection(self.obj, _selection.obj if _selection else None)
        return ret

    def Run(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsCommandRun(self.obj)
        return ret

class PsProgressControl(_PdfixBase):
    def __init__(self, _obj):
        super(PsProgressControl, self).__init__(_obj)

    def SetCancelProc(self, _cancel_proc, _cancel_data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsProgressControlSetCancelProc(self.obj, _cancel_proc, _cancel_data)
        return ret

    def SetData(self, _client_data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsProgressControlSetData(self.obj, _client_data)
        return ret

    def GetData(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PsProgressControlGetData(self.obj)
        return ret

    def StartProcess(self, _steps: int) -> int: 
        global PdfixLib
        ret = PdfixLib.PsProgressControlStartProcess(self.obj, _steps)
        return ret

    def EndProcess(self, _process_id: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsProgressControlEndProcess(self.obj, _process_id)
        return ret

    def Step(self, _process_id: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsProgressControlStep(self.obj, _process_id)
        return ret

    def SetText(self, _text) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsProgressControlSetText(self.obj, _text)
        return ret

    def GetText(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PsProgressControlGetText(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PsProgressControlGetText(self.obj, _buffer, _len)
        return _buffer.value

    def GetState(self) -> float: 
        global PdfixLib
        ret = PdfixLib.PsProgressControlGetState(self.obj)
        return ret

    def Cancel(self) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsProgressControlCancel(self.obj)
        return ret

class PsRenderDeviceContext(_PdfixBase):
    def __init__(self, _obj):
        super(PsRenderDeviceContext, self).__init__(_obj)

    def GetType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PsRenderDeviceContextGetType(self.obj)
        return ret

class PsImage(_PdfixBase):
    def __init__(self, _obj):
        super(PsImage, self).__init__(_obj)

    def Destroy(self): 
        global PdfixLib
        ret = PdfixLib.PsImageDestroy(self.obj)
        return ret

    def Save(self, _path, _params: PdfImageParams) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsImageSave(self.obj, _path, _params.GetIntStruct() if _params else None)
        return ret

    def SaveRect(self, _path, _params: PdfImageParams, _dev_rect: PdfDevRect) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsImageSaveRect(self.obj, _path, _params.GetIntStruct() if _params else None, _dev_rect.GetIntStruct() if _dev_rect else None)
        return ret

    def SaveToStream(self, _stream: PsStream, _params: PdfImageParams) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsImageSaveToStream(self.obj, _stream.obj if _stream else None, _params.GetIntStruct() if _params else None)
        return ret

    def SaveRectToStream(self, _stream: PsStream, _params: PdfImageParams, _dev_rect: PdfDevRect) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsImageSaveRectToStream(self.obj, _stream.obj if _stream else None, _params.GetIntStruct() if _params else None, _dev_rect.GetIntStruct() if _dev_rect else None)
        return ret

    def GetPointColor(self, _point: PdfDevPoint): 
        global PdfixLib
        result = PdfRGB()
        _color = result.GetIntStruct()
        PdfixLib.PsImageGetPointColor(self.obj, _point.GetIntStruct(), _color)
        result.SetIntStruct(_color)
        return result

    def SaveDataToStream(self, _stream: PsStream) -> bool: 
        global PdfixLib
        ret = PdfixLib.PsImageSaveDataToStream(self.obj, _stream.obj if _stream else None)
        return ret

class PsSysFont(_PdfixBase):
    def __init__(self, _obj):
        super(PsSysFont, self).__init__(_obj)

    def Destroy(self): 
        global PdfixLib
        ret = PdfixLib.PsSysFontDestroy(self.obj)
        return ret

class Pdfix(_PdfixBase):
    def __init__(self, _obj):
        super(Pdfix, self).__init__(_obj)

    def Destroy(self): 
        global PdfixLib
        ret = PdfixLib.PdfixDestroy(self.obj)
        return ret

    def GetAuthorization(self) -> PsAuthorization: 
        global PdfixLib
        ret = PdfixLib.PdfixGetAuthorization(self.obj)
        if ret:
            return PsAuthorization(ret)
        else:
            return None

    def GetStandardAuthorization(self) -> PsStandardAuthorization: 
        global PdfixLib
        ret = PdfixLib.PdfixGetStandardAuthorization(self.obj)
        if ret:
            return PsStandardAuthorization(ret)
        else:
            return None

    def GetAccountAuthorization(self) -> PsAccountAuthorization: 
        global PdfixLib
        ret = PdfixLib.PdfixGetAccountAuthorization(self.obj)
        if ret:
            return PsAccountAuthorization(ret)
        else:
            return None

    def GetErrorType(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfixGetErrorType(self.obj)
        return ret

    def GetError(self): 
        global PdfixLib
        ret = PdfixLib.PdfixGetError(self.obj)
        return ret

    def GetErrorDescription(self): 
        global PdfixLib
        ret = PdfixLib.PdfixGetErrorDescription(self.obj)
        return ret

    def SetError(self, _type: int, _error, _description): 
        global PdfixLib
        ret = PdfixLib.PdfixSetError(self.obj, _type, _error, _description)
        return ret

    def GetProductName(self): 
        global PdfixLib
        ret = PdfixLib.PdfixGetProductName(self.obj)
        return ret

    def GetProductUrl(self): 
        global PdfixLib
        ret = PdfixLib.PdfixGetProductUrl(self.obj)
        return ret

    def GetVersionMajor(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfixGetVersionMajor(self.obj)
        return ret

    def GetVersionMinor(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfixGetVersionMinor(self.obj)
        return ret

    def GetVersionPatch(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfixGetVersionPatch(self.obj)
        return ret

    def CreateDoc(self) -> PdfDoc: 
        global PdfixLib
        ret = PdfixLib.PdfixCreateDoc(self.obj)
        if ret:
            return PdfDoc(ret)
        else:
            return None

    def OpenDoc(self, _path, _password) -> PdfDoc: 
        global PdfixLib
        ret = PdfixLib.PdfixOpenDoc(self.obj, _path, _password)
        if ret:
            return PdfDoc(ret)
        else:
            return None

    def OpenDocFromStream(self, _stream: PsStream, _password) -> PdfDoc: 
        global PdfixLib
        ret = PdfixLib.PdfixOpenDocFromStream(self.obj, _stream.obj if _stream else None, _password)
        if ret:
            return PdfDoc(ret)
        else:
            return None

    def CreateDigSig(self) -> PdfDigSig: 
        global PdfixLib
        ret = PdfixLib.PdfixCreateDigSig(self.obj)
        if ret:
            return PdfDigSig(ret)
        else:
            return None

    def CreateCustomDigSig(self) -> PdfCustomDigSig: 
        global PdfixLib
        ret = PdfixLib.PdfixCreateCustomDigSig(self.obj)
        if ret:
            return PdfCustomDigSig(ret)
        else:
            return None

    def CreateStandardSecurityHandler(self, _user_password, _owner_password, _params: PdfStandardSecurityParams) -> PdfStandardSecurityHandler: 
        global PdfixLib
        ret = PdfixLib.PdfixCreateStandardSecurityHandler(self.obj, _user_password, _owner_password, _params.GetIntStruct() if _params else None)
        if ret:
            return PdfStandardSecurityHandler(ret)
        else:
            return None

    def CreateCustomSecurityHandler(self, _name, _client_data: int) -> PdfCustomSecurityHandler: 
        global PdfixLib
        ret = PdfixLib.PdfixCreateCustomSecurityHandler(self.obj, _name, _client_data)
        if ret:
            return PdfCustomSecurityHandler(ret)
        else:
            return None

    def RegisterSecurityHandler(self, _proc, _name, _client_data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfixRegisterSecurityHandler(self.obj, _proc, _name, _client_data)
        return ret

    def RegisterAnnotHandler(self, _type) -> PdfAnnotHandler: 
        global PdfixLib
        ret = PdfixLib.PdfixRegisterAnnotHandler(self.obj, _type)
        if ret:
            return PdfAnnotHandler(ret)
        else:
            return None

    def RegisterActionHandler(self, _type) -> PdfActionHandler: 
        global PdfixLib
        ret = PdfixLib.PdfixRegisterActionHandler(self.obj, _type)
        if ret:
            return PdfActionHandler(ret)
        else:
            return None

    def CreateRegex(self) -> PsRegex: 
        global PdfixLib
        ret = PdfixLib.PdfixCreateRegex(self.obj)
        if ret:
            return PsRegex(ret)
        else:
            return None

    def CreateFileStream(self, _path, _mode: int) -> PsFileStream: 
        global PdfixLib
        ret = PdfixLib.PdfixCreateFileStream(self.obj, _path, _mode)
        if ret:
            return PsFileStream(ret)
        else:
            return None

    def CreateMemStream(self) -> PsMemoryStream: 
        global PdfixLib
        ret = PdfixLib.PdfixCreateMemStream(self.obj)
        if ret:
            return PsMemoryStream(ret)
        else:
            return None

    def CreateCustomStream(self, _read_proc, _client_data: int) -> PsCustomStream: 
        global PdfixLib
        ret = PdfixLib.PdfixCreateCustomStream(self.obj, _read_proc, _client_data)
        if ret:
            return PsCustomStream(ret)
        else:
            return None

    def RegisterEvent(self, _type: int, _proc, _data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfixRegisterEvent(self.obj, _type, _proc, _data)
        return ret

    def UnregisterEvent(self, _type: int, _proc, _data: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfixUnregisterEvent(self.obj, _type, _proc, _data)
        return ret

    def ReadImageInfo(self, _image_stream: PsStream, _format: int) -> bool: 
        global PdfixLib
        result = PsImageInfo()
        _info = result.GetIntStruct()
        PdfixLib.PdfixReadImageInfo(self.obj, _image_stream.GetIntStruct(), _format, _info)
        result.SetIntStruct(_info)
        return result

    def CreateImage(self, _width: int, _height: int, _format: int) -> PsImage: 
        global PdfixLib
        ret = PdfixLib.PdfixCreateImage(self.obj, _width, _height, _format)
        if ret:
            return PsImage(ret)
        else:
            return None

    def CreateRenderDeviceContext(self, _device: int, _type: int) -> PsRenderDeviceContext: 
        global PdfixLib
        ret = PdfixLib.PdfixCreateRenderDeviceContext(self.obj, _device, _type)
        if ret:
            return PsRenderDeviceContext(ret)
        else:
            return None

    def RegisterPlugin(self, _plugin: PdfixPlugin, _name) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfixRegisterPlugin(self.obj, _plugin.obj if _plugin else None, _name)
        return ret

    def GetPluginByName(self, _name) -> PdfixPlugin: 
        global PdfixLib
        ret = PdfixLib.PdfixGetPluginByName(self.obj, _name)
        if ret:
            return PdfixPlugin(ret)
        else:
            return None

    def GetEvent(self) -> PsEvent: 
        global PdfixLib
        ret = PdfixLib.PdfixGetEvent(self.obj)
        if ret:
            return PsEvent(ret)
        else:
            return None

    def FindSysFont(self, _font_family, _font_flags: int, _codepage: int) -> PsSysFont: 
        global PdfixLib
        ret = PdfixLib.PdfixFindSysFont(self.obj, _font_family, _font_flags, _codepage)
        if ret:
            return PsSysFont(ret)
        else:
            return None

    def LoadSettingsFromStream(self, _settings: PsStream, _format: int) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfixLoadSettingsFromStream(self.obj, _settings.obj if _settings else None, _format)
        return ret

    def GetTags(self, _version: int) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfixGetTags(self.obj, _version, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfixGetTags(self.obj, _version, _buffer, _len)
        return _buffer.value

    def GetSysFonts(self) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfixGetSysFonts(self.obj, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfixGetSysFonts(self.obj, _buffer, _len)
        return _buffer.value

    def GetRtlText(self, _text) -> str: 
        global PdfixLib
        _len = PdfixLib.PdfixGetRtlText(self.obj, _text, None, 0)
        _buffer = create_unicode_buffer(_len)
        _len = PdfixLib.PdfixGetRtlText(self.obj, _text, _buffer, _len)
        return _buffer.value

class PdfixPlugin(_PdfixBase):
    def __init__(self, _obj):
        super(PdfixPlugin, self).__init__(_obj)

    def Destroy(self): 
        global PdfixLib
        ret = PdfixLib.PdfixPluginDestroy(self.obj)
        return ret

    def Initialize(self, _pdfix: Pdfix) -> bool: 
        global PdfixLib
        ret = PdfixLib.PdfixPluginInitialize(self.obj, _pdfix.obj if _pdfix else None)
        return ret

    def GetVersionMajor(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfixPluginGetVersionMajor(self.obj)
        return ret

    def GetVersionMinor(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfixPluginGetVersionMinor(self.obj)
        return ret

    def GetVersionPatch(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfixPluginGetVersionPatch(self.obj)
        return ret

    def GetPdfixVersionMajor(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfixPluginGetPdfixVersionMajor(self.obj)
        return ret

    def GetPdfixVersionMinor(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfixPluginGetPdfixVersionMinor(self.obj)
        return ret

    def GetPdfixVersionPatch(self) -> int: 
        global PdfixLib
        ret = PdfixLib.PdfixPluginGetPdfixVersionPatch(self.obj)
        return ret

    def GetPdfix(self) -> Pdfix: 
        global PdfixLib
        ret = PdfixLib.PdfixPluginGetPdfix(self.obj)
        if ret:
            return Pdfix(ret)
        else:
            return None

def GetPdfix():
    global PdfixLib
    obj = PdfixLib.GetPdfix()
    return Pdfix(obj)

PdfixLib = None

def Pdfix_init(path):
    global PdfixLib
    PdfixLib = cdll.LoadLibrary(path)
    if PdfixLib is None:
        raise Exception("LoadLibrary fail")
    PdfixLib.PdsObjectGetObjectType.restype = c_int
    PdfixLib.PdsObjectGetObjectType.argtypes = [c_void_p]
    PdfixLib.PdsObjectGetId.restype = c_int
    PdfixLib.PdsObjectGetId.argtypes = [c_void_p]
    PdfixLib.PdsObjectGetGenId.restype = c_int
    PdfixLib.PdsObjectGetGenId.argtypes = [c_void_p]
    PdfixLib.PdsObjectGetDoc.restype = c_void_p
    PdfixLib.PdsObjectGetDoc.argtypes = [c_void_p]
    PdfixLib.PdsObjectClone.restype = c_void_p
    PdfixLib.PdsObjectClone.argtypes = [c_void_p, c_int]
    PdfixLib.PdsObjectRegisterEvent.restype = c_int
    PdfixLib.PdsObjectRegisterEvent.argtypes = [c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdsObjectUnregisterEvent.restype = c_int
    PdfixLib.PdsObjectUnregisterEvent.argtypes = [c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdsBooleanGetValue.restype = c_int
    PdfixLib.PdsBooleanGetValue.argtypes = [c_void_p]
    PdfixLib.PdsNumberIsIntegerValue.restype = c_int
    PdfixLib.PdsNumberIsIntegerValue.argtypes = [c_void_p]
    PdfixLib.PdsNumberGetIntegerValue.restype = c_int
    PdfixLib.PdsNumberGetIntegerValue.argtypes = [c_void_p]
    PdfixLib.PdsNumberGetValue.restype = c_float
    PdfixLib.PdsNumberGetValue.argtypes = [c_void_p]
    PdfixLib.PdsStringGetValue.restype = c_int
    PdfixLib.PdsStringGetValue.argtypes = [c_void_p, c_char_p, c_int]
    PdfixLib.PdsStringGetText.restype = c_int
    PdfixLib.PdsStringGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStringIsHexValue.restype = c_int
    PdfixLib.PdsStringIsHexValue.argtypes = [c_void_p]
    PdfixLib.PdsNameGetValue.restype = c_int
    PdfixLib.PdsNameGetValue.argtypes = [c_void_p, c_char_p, c_int]
    PdfixLib.PdsNameGetText.restype = c_int
    PdfixLib.PdsNameGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsArrayGetNumObjects.restype = c_int
    PdfixLib.PdsArrayGetNumObjects.argtypes = [c_void_p]
    PdfixLib.PdsArrayGet.restype = c_void_p
    PdfixLib.PdsArrayGet.argtypes = [c_void_p, c_int]
    PdfixLib.PdsArrayPut.restype = c_int
    PdfixLib.PdsArrayPut.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PdsArrayPutNumber.restype = c_int
    PdfixLib.PdsArrayPutNumber.argtypes = [c_void_p, c_int, c_float]
    PdfixLib.PdsArrayPutName.restype = c_int
    PdfixLib.PdsArrayPutName.argtypes = [c_void_p, c_int, c_wchar_p]
    PdfixLib.PdsArrayPutString.restype = c_int
    PdfixLib.PdsArrayPutString.argtypes = [c_void_p, c_int, c_wchar_p]
    PdfixLib.PdsArrayInsert.restype = c_int
    PdfixLib.PdsArrayInsert.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PdsArrayInsertDict.restype = c_void_p
    PdfixLib.PdsArrayInsertDict.argtypes = [c_void_p, c_int]
    PdfixLib.PdsArrayInsertArray.restype = c_void_p
    PdfixLib.PdsArrayInsertArray.argtypes = [c_void_p, c_int]
    PdfixLib.PdsArrayRemoveNth.restype = c_int
    PdfixLib.PdsArrayRemoveNth.argtypes = [c_void_p, c_int]
    PdfixLib.PdsArrayGetDictionary.restype = c_void_p
    PdfixLib.PdsArrayGetDictionary.argtypes = [c_void_p, c_int]
    PdfixLib.PdsArrayGetArray.restype = c_void_p
    PdfixLib.PdsArrayGetArray.argtypes = [c_void_p, c_int]
    PdfixLib.PdsArrayGetStream.restype = c_void_p
    PdfixLib.PdsArrayGetStream.argtypes = [c_void_p, c_int]
    PdfixLib.PdsArrayGetString.restype = c_int
    PdfixLib.PdsArrayGetString.argtypes = [c_void_p, c_int, c_char_p, c_int]
    PdfixLib.PdsArrayGetText.restype = c_int
    PdfixLib.PdsArrayGetText.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdsArrayGetNumber.restype = c_float
    PdfixLib.PdsArrayGetNumber.argtypes = [c_void_p, c_int]
    PdfixLib.PdsArrayGetInteger.restype = c_int
    PdfixLib.PdsArrayGetInteger.argtypes = [c_void_p, c_int]
    PdfixLib.PdsDictionaryKnown.restype = c_int
    PdfixLib.PdsDictionaryKnown.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsDictionaryGetNumKeys.restype = c_int
    PdfixLib.PdsDictionaryGetNumKeys.argtypes = [c_void_p]
    PdfixLib.PdsDictionaryGetKey.restype = c_int
    PdfixLib.PdsDictionaryGetKey.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdsDictionaryGet.restype = c_void_p
    PdfixLib.PdsDictionaryGet.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsDictionaryPut.restype = c_int
    PdfixLib.PdsDictionaryPut.argtypes = [c_void_p, c_wchar_p, c_void_p]
    PdfixLib.PdsDictionaryPutBool.restype = c_int
    PdfixLib.PdsDictionaryPutBool.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsDictionaryPutName.restype = c_int
    PdfixLib.PdsDictionaryPutName.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdsDictionaryPutString.restype = c_int
    PdfixLib.PdsDictionaryPutString.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdsDictionaryPutNumber.restype = c_int
    PdfixLib.PdsDictionaryPutNumber.argtypes = [c_void_p, c_wchar_p, c_float]
    PdfixLib.PdsDictionaryGetRect.restype = c_int
    PdfixLib.PdsDictionaryGetRect.argtypes = [c_void_p, c_wchar_p, POINTER(zz_PdfRect)]
    PdfixLib.PdsDictionaryPutRect.restype = c_int
    PdfixLib.PdsDictionaryPutRect.argtypes = [c_void_p, c_wchar_p, POINTER(zz_PdfRect)]
    PdfixLib.PdsDictionaryGetMatrix.restype = c_int
    PdfixLib.PdsDictionaryGetMatrix.argtypes = [c_void_p, c_wchar_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdsDictionaryPutMatrix.restype = c_int
    PdfixLib.PdsDictionaryPutMatrix.argtypes = [c_void_p, c_wchar_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdsDictionaryPutDict.restype = c_void_p
    PdfixLib.PdsDictionaryPutDict.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsDictionaryPutArray.restype = c_void_p
    PdfixLib.PdsDictionaryPutArray.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsDictionaryGetDictionary.restype = c_void_p
    PdfixLib.PdsDictionaryGetDictionary.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsDictionaryGetArray.restype = c_void_p
    PdfixLib.PdsDictionaryGetArray.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsDictionaryGetStream.restype = c_void_p
    PdfixLib.PdsDictionaryGetStream.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsDictionaryGetString.restype = c_int
    PdfixLib.PdsDictionaryGetString.argtypes = [c_void_p, c_wchar_p, c_char_p, c_int]
    PdfixLib.PdsDictionaryGetText.restype = c_int
    PdfixLib.PdsDictionaryGetText.argtypes = [c_void_p, c_wchar_p, c_wchar_p, c_int]
    PdfixLib.PdsDictionaryGetNumber.restype = c_float
    PdfixLib.PdsDictionaryGetNumber.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsDictionaryGetInteger.restype = c_int
    PdfixLib.PdsDictionaryGetInteger.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsDictionaryGetBoolean.restype = c_int
    PdfixLib.PdsDictionaryGetBoolean.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsDictionaryRemoveKey.restype = c_int
    PdfixLib.PdsDictionaryRemoveKey.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsStreamGetStreamDict.restype = c_void_p
    PdfixLib.PdsStreamGetStreamDict.argtypes = [c_void_p]
    PdfixLib.PdsStreamGetRawDataSize.restype = c_int
    PdfixLib.PdsStreamGetRawDataSize.argtypes = [c_void_p]
    PdfixLib.PdsStreamIsEof.restype = c_int
    PdfixLib.PdsStreamIsEof.argtypes = [c_void_p]
    PdfixLib.PdsStreamGetSize.restype = c_int
    PdfixLib.PdsStreamGetSize.argtypes = [c_void_p]
    PdfixLib.PdsStreamRead.restype = c_int
    PdfixLib.PdsStreamRead.argtypes = [c_void_p, c_int, POINTER(c_ubyte), c_int]
    PdfixLib.PdsStreamGetPos.restype = c_int
    PdfixLib.PdsStreamGetPos.argtypes = [c_void_p]
    PdfixLib.PdsContentAddNewText.restype = c_void_p
    PdfixLib.PdsContentAddNewText.argtypes = [c_void_p, c_int, c_void_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdsContentAddNewPath.restype = c_void_p
    PdfixLib.PdsContentAddNewPath.argtypes = [c_void_p, c_int, POINTER(zz_PdfMatrix)]
    PdfixLib.PdsContentAddNewImage.restype = c_void_p
    PdfixLib.PdsContentAddNewImage.argtypes = [c_void_p, c_int, c_void_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdsContentAddNewForm.restype = c_void_p
    PdfixLib.PdsContentAddNewForm.argtypes = [c_void_p, c_int, c_void_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdsContentRemoveObject.restype = c_int
    PdfixLib.PdsContentRemoveObject.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdsContentGetNumObjects.restype = c_int
    PdfixLib.PdsContentGetNumObjects.argtypes = [c_void_p]
    PdfixLib.PdsContentGetObject.restype = c_void_p
    PdfixLib.PdsContentGetObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdsContentToObject.restype = c_void_p
    PdfixLib.PdsContentToObject.argtypes = [c_void_p, c_void_p, POINTER(zz_PdsContentParams)]
    PdfixLib.PdsContentGetPage.restype = c_void_p
    PdfixLib.PdsContentGetPage.argtypes = [c_void_p]
    PdfixLib.PdsContentGetForm.restype = c_void_p
    PdfixLib.PdsContentGetForm.argtypes = [c_void_p]
    PdfixLib.PdsContentRegisterEvent.restype = c_int
    PdfixLib.PdsContentRegisterEvent.argtypes = [c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdsContentUnregisterEvent.restype = c_int
    PdfixLib.PdsContentUnregisterEvent.argtypes = [c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdsPageObjectGetObjectType.restype = c_int
    PdfixLib.PdsPageObjectGetObjectType.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectGetBBox.restype = c_int
    PdfixLib.PdsPageObjectGetBBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdsPageObjectGetQuad.restype = c_int
    PdfixLib.PdsPageObjectGetQuad.argtypes = [c_void_p, POINTER(zz_PdfQuad)]
    PdfixLib.PdsPageObjectGetId.restype = c_int
    PdfixLib.PdsPageObjectGetId.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectGetStateFlags.restype = c_int
    PdfixLib.PdsPageObjectGetStateFlags.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectSetStateFlags.restype = c_int
    PdfixLib.PdsPageObjectSetStateFlags.argtypes = [c_void_p, c_int]
    PdfixLib.PdsPageObjectGetStructObject.restype = c_void_p
    PdfixLib.PdsPageObjectGetStructObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdsPageObjectGetContentMark.restype = c_void_p
    PdfixLib.PdsPageObjectGetContentMark.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectGetMcid.restype = c_int
    PdfixLib.PdsPageObjectGetMcid.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectRemoveTags.restype = c_int
    PdfixLib.PdsPageObjectRemoveTags.argtypes = [c_void_p, c_int]
    PdfixLib.PdsPageObjectGetPage.restype = c_void_p
    PdfixLib.PdsPageObjectGetPage.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectGetContentStreamIndex.restype = c_int
    PdfixLib.PdsPageObjectGetContentStreamIndex.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectGetParentContent.restype = c_void_p
    PdfixLib.PdsPageObjectGetParentContent.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectGetGState.restype = c_int
    PdfixLib.PdsPageObjectGetGState.argtypes = [c_void_p, POINTER(zz_PdfGraphicState)]
    PdfixLib.PdsPageObjectSetGState.restype = c_int
    PdfixLib.PdsPageObjectSetGState.argtypes = [c_void_p, POINTER(zz_PdfGraphicState)]
    PdfixLib.PdsPageObjectTransformCTM.restype = c_int
    PdfixLib.PdsPageObjectTransformCTM.argtypes = [c_void_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdsPageObjectMoveToObject.restype = c_int
    PdfixLib.PdsPageObjectMoveToObject.argtypes = [c_void_p, c_void_p, c_int, c_int, c_int]
    PdfixLib.PdsPageObjectMoveToContent.restype = c_int
    PdfixLib.PdsPageObjectMoveToContent.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdsPageObjectCopyToContent.restype = c_void_p
    PdfixLib.PdsPageObjectCopyToContent.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdsPageObjectGetDoc.restype = c_void_p
    PdfixLib.PdsPageObjectGetDoc.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectGetNumEqualTags.restype = c_int
    PdfixLib.PdsPageObjectGetNumEqualTags.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdsPageObjectGetOperatorId.restype = c_int
    PdfixLib.PdsPageObjectGetOperatorId.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectGetContentId.restype = c_int
    PdfixLib.PdsPageObjectGetContentId.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectGetNumContentItemIds.restype = c_int
    PdfixLib.PdsPageObjectGetNumContentItemIds.argtypes = [c_void_p]
    PdfixLib.PdsPageObjectGetContentItemId.restype = c_int
    PdfixLib.PdsPageObjectGetContentItemId.argtypes = [c_void_p, c_int]
    PdfixLib.PdsPageObjectRegisterEvent.restype = c_int
    PdfixLib.PdsPageObjectRegisterEvent.argtypes = [c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdsPageObjectUnregisterEvent.restype = c_int
    PdfixLib.PdsPageObjectUnregisterEvent.argtypes = [c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdsTextGetText.restype = c_int
    PdfixLib.PdsTextGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsTextGetTextEx.restype = c_int
    PdfixLib.PdsTextGetTextEx.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdsTextSetText.restype = c_int
    PdfixLib.PdsTextSetText.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsTextGetTextState.restype = c_int
    PdfixLib.PdsTextGetTextState.argtypes = [c_void_p, POINTER(zz_PdfTextState)]
    PdfixLib.PdsTextSetTextState.restype = c_int
    PdfixLib.PdsTextSetTextState.argtypes = [c_void_p, POINTER(zz_PdfTextState)]
    PdfixLib.PdsTextGetTextMatrix.restype = c_int
    PdfixLib.PdsTextGetTextMatrix.argtypes = [c_void_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdsTextGetNumChars.restype = c_int
    PdfixLib.PdsTextGetNumChars.argtypes = [c_void_p]
    PdfixLib.PdsTextGetCharCode.restype = c_int
    PdfixLib.PdsTextGetCharCode.argtypes = [c_void_p, c_int]
    PdfixLib.PdsTextGetCharText.restype = c_int
    PdfixLib.PdsTextGetCharText.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdsTextGetCharBBox.restype = c_int
    PdfixLib.PdsTextGetCharBBox.argtypes = [c_void_p, c_int, POINTER(zz_PdfRect)]
    PdfixLib.PdsTextGetCharQuad.restype = c_int
    PdfixLib.PdsTextGetCharQuad.argtypes = [c_void_p, c_int, POINTER(zz_PdfQuad)]
    PdfixLib.PdsTextGetCharAdvanceWidth.restype = c_float
    PdfixLib.PdsTextGetCharAdvanceWidth.argtypes = [c_void_p, c_int]
    PdfixLib.PdsTextSplitAtChar.restype = c_void_p
    PdfixLib.PdsTextSplitAtChar.argtypes = [c_void_p, c_int]
    PdfixLib.PdsTextGetCharStateFlags.restype = c_int
    PdfixLib.PdsTextGetCharStateFlags.argtypes = [c_void_p, c_int]
    PdfixLib.PdsTextSetCharStateFlags.restype = c_int
    PdfixLib.PdsTextSetCharStateFlags.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdsFormGetContent.restype = c_void_p
    PdfixLib.PdsFormGetContent.argtypes = [c_void_p]
    PdfixLib.PdsFormGetMatrix.restype = c_int
    PdfixLib.PdsFormGetMatrix.argtypes = [c_void_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdsFormGetObject.restype = c_void_p
    PdfixLib.PdsFormGetObject.argtypes = [c_void_p]
    PdfixLib.PdsPathGetNumPathPoints.restype = c_int
    PdfixLib.PdsPathGetNumPathPoints.argtypes = [c_void_p]
    PdfixLib.PdsPathGetPathPoint.restype = c_void_p
    PdfixLib.PdsPathGetPathPoint.argtypes = [c_void_p, c_int]
    PdfixLib.PdsPathSetStroke.restype = c_int
    PdfixLib.PdsPathSetStroke.argtypes = [c_void_p, c_int]
    PdfixLib.PdsPathSetFillType.restype = c_int
    PdfixLib.PdsPathSetFillType.argtypes = [c_void_p, c_int]
    PdfixLib.PdsPathMoveTo.restype = c_int
    PdfixLib.PdsPathMoveTo.argtypes = [c_void_p, POINTER(zz_PdfPoint)]
    PdfixLib.PdsPathLineTo.restype = c_int
    PdfixLib.PdsPathLineTo.argtypes = [c_void_p, POINTER(zz_PdfPoint)]
    PdfixLib.PdsPathCurveTo.restype = c_int
    PdfixLib.PdsPathCurveTo.argtypes = [c_void_p, POINTER(zz_PdfPoint), POINTER(zz_PdfPoint), POINTER(zz_PdfPoint)]
    PdfixLib.PdsPathArcTo.restype = c_int
    PdfixLib.PdsPathArcTo.argtypes = [c_void_p, POINTER(zz_PdfPoint), POINTER(zz_PdfPoint), c_float, c_int, c_int]
    PdfixLib.PdsPathClosePath.restype = c_int
    PdfixLib.PdsPathClosePath.argtypes = [c_void_p]
    PdfixLib.PdsPathPointGetType.restype = c_int
    PdfixLib.PdsPathPointGetType.argtypes = [c_void_p]
    PdfixLib.PdsPathPointGetPoint.restype = c_int
    PdfixLib.PdsPathPointGetPoint.argtypes = [c_void_p, POINTER(zz_PdfPoint)]
    PdfixLib.PdsPathPointIsClosed.restype = c_int
    PdfixLib.PdsPathPointIsClosed.argtypes = [c_void_p]
    PdfixLib.PdsSoftMaskGetDataStm.restype = c_void_p
    PdfixLib.PdsSoftMaskGetDataStm.argtypes = [c_void_p]
    PdfixLib.PdsImageGetDataStm.restype = c_void_p
    PdfixLib.PdsImageGetDataStm.argtypes = [c_void_p]
    PdfixLib.PdsImageGetSMask.restype = c_void_p
    PdfixLib.PdsImageGetSMask.argtypes = [c_void_p]
    PdfixLib.PdsImageHasSMask.restype = c_int
    PdfixLib.PdsImageHasSMask.argtypes = [c_void_p]
    PdfixLib.PdsContentMarkGetNumTags.restype = c_int
    PdfixLib.PdsContentMarkGetNumTags.argtypes = [c_void_p]
    PdfixLib.PdsContentMarkGetTagName.restype = c_int
    PdfixLib.PdsContentMarkGetTagName.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdsContentMarkSetTagName.restype = c_int
    PdfixLib.PdsContentMarkSetTagName.argtypes = [c_void_p, c_int, c_wchar_p]
    PdfixLib.PdsContentMarkGetTagObject.restype = c_void_p
    PdfixLib.PdsContentMarkGetTagObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdsContentMarkSetTagObject.restype = c_int
    PdfixLib.PdsContentMarkSetTagObject.argtypes = [c_void_p, c_int, c_void_p, c_int]
    PdfixLib.PdsContentMarkGetTagMcid.restype = c_int
    PdfixLib.PdsContentMarkGetTagMcid.argtypes = [c_void_p]
    PdfixLib.PdsContentMarkGetTagArtifact.restype = c_int
    PdfixLib.PdsContentMarkGetTagArtifact.argtypes = [c_void_p]
    PdfixLib.PdsContentMarkAddTag.restype = c_int
    PdfixLib.PdsContentMarkAddTag.argtypes = [c_void_p, c_wchar_p, c_void_p, c_int]
    PdfixLib.PdsContentMarkInsertTag.restype = c_int
    PdfixLib.PdsContentMarkInsertTag.argtypes = [c_void_p, c_int, c_wchar_p, c_void_p, c_int]
    PdfixLib.PdsContentMarkRemoveTag.restype = c_int
    PdfixLib.PdsContentMarkRemoveTag.argtypes = [c_void_p, c_int]
    PdfixLib.PdeWordListGetNumWords.restype = c_int
    PdfixLib.PdeWordListGetNumWords.argtypes = [c_void_p]
    PdfixLib.PdeWordListGetWord.restype = c_void_p
    PdfixLib.PdeWordListGetWord.argtypes = [c_void_p, c_int]
    PdfixLib.PdeWordListGetRefNum.restype = c_int
    PdfixLib.PdeWordListGetRefNum.argtypes = [c_void_p]
    PdfixLib.PdeWordListRelease.restype = c_int
    PdfixLib.PdeWordListRelease.argtypes = [c_void_p]
    PdfixLib.PdeElementGetType.restype = c_int
    PdfixLib.PdeElementGetType.argtypes = [c_void_p]
    PdfixLib.PdeElementGetBBox.restype = c_int
    PdfixLib.PdeElementGetBBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdeElementSetBBox.restype = c_int
    PdfixLib.PdeElementSetBBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdeElementGetQuad.restype = c_int
    PdfixLib.PdeElementGetQuad.argtypes = [c_void_p, POINTER(zz_PdfQuad)]
    PdfixLib.PdeElementGetId.restype = c_int
    PdfixLib.PdeElementGetId.argtypes = [c_void_p]
    PdfixLib.PdeElementGetGraphicState.restype = c_int
    PdfixLib.PdeElementGetGraphicState.argtypes = [c_void_p, POINTER(zz_PdeGraphicState)]
    PdfixLib.PdeElementGetNumChildren.restype = c_int
    PdfixLib.PdeElementGetNumChildren.argtypes = [c_void_p]
    PdfixLib.PdeElementGetChild.restype = c_void_p
    PdfixLib.PdeElementGetChild.argtypes = [c_void_p, c_int]
    PdfixLib.PdeElementGetAlignment.restype = c_int
    PdfixLib.PdeElementGetAlignment.argtypes = [c_void_p]
    PdfixLib.PdeElementGetAngle.restype = c_float
    PdfixLib.PdeElementGetAngle.argtypes = [c_void_p]
    PdfixLib.PdeElementSetData.restype = c_int
    PdfixLib.PdeElementSetData.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdeElementGetData.restype = c_void_p
    PdfixLib.PdeElementGetData.argtypes = [c_void_p]
    PdfixLib.PdeElementSetAlt.restype = c_int
    PdfixLib.PdeElementSetAlt.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdeElementSetActualText.restype = c_int
    PdfixLib.PdeElementSetActualText.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdeElementGetTag.restype = c_int
    PdfixLib.PdeElementGetTag.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdeElementSetTag.restype = c_int
    PdfixLib.PdeElementSetTag.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdeElementGetTagId.restype = c_int
    PdfixLib.PdeElementGetTagId.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdeElementSetTagId.restype = c_int
    PdfixLib.PdeElementSetTagId.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdeElementGetFlags.restype = c_int
    PdfixLib.PdeElementGetFlags.argtypes = [c_void_p]
    PdfixLib.PdeElementSetFlags.restype = c_int
    PdfixLib.PdeElementSetFlags.argtypes = [c_void_p, c_int]
    PdfixLib.PdeElementGetStateFlags.restype = c_int
    PdfixLib.PdeElementGetStateFlags.argtypes = [c_void_p]
    PdfixLib.PdeElementSetStateFlags.restype = c_int
    PdfixLib.PdeElementSetStateFlags.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdeElementGetNumPageObjects.restype = c_int
    PdfixLib.PdeElementGetNumPageObjects.argtypes = [c_void_p]
    PdfixLib.PdeElementGetPageObject.restype = c_void_p
    PdfixLib.PdeElementGetPageObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdeElementGetPageMap.restype = c_void_p
    PdfixLib.PdeElementGetPageMap.argtypes = [c_void_p]
    PdfixLib.PdeElementGetLabelType.restype = c_int
    PdfixLib.PdeElementGetLabelType.argtypes = [c_void_p]
    PdfixLib.PdeElementSetLabelType.restype = c_int
    PdfixLib.PdeElementSetLabelType.argtypes = [c_void_p, c_int]
    PdfixLib.PdeAnnotGetAnnot.restype = c_void_p
    PdfixLib.PdeAnnotGetAnnot.argtypes = [c_void_p]
    PdfixLib.PdeImageGetImageType.restype = c_int
    PdfixLib.PdeImageGetImageType.argtypes = [c_void_p]
    PdfixLib.PdeImageGetCaption.restype = c_void_p
    PdfixLib.PdeImageGetCaption.argtypes = [c_void_p]
    PdfixLib.PdeCellGetRowNum.restype = c_int
    PdfixLib.PdeCellGetRowNum.argtypes = [c_void_p]
    PdfixLib.PdeCellSetRowNum.restype = c_int
    PdfixLib.PdeCellSetRowNum.argtypes = [c_void_p, c_int]
    PdfixLib.PdeCellGetColNum.restype = c_int
    PdfixLib.PdeCellGetColNum.argtypes = [c_void_p]
    PdfixLib.PdeCellSetColNum.restype = c_int
    PdfixLib.PdeCellSetColNum.argtypes = [c_void_p, c_int]
    PdfixLib.PdeCellGetHeader.restype = c_int
    PdfixLib.PdeCellGetHeader.argtypes = [c_void_p]
    PdfixLib.PdeCellSetHeader.restype = c_int
    PdfixLib.PdeCellSetHeader.argtypes = [c_void_p, c_int]
    PdfixLib.PdeCellGetHeaderScope.restype = c_int
    PdfixLib.PdeCellGetHeaderScope.argtypes = [c_void_p]
    PdfixLib.PdeCellSetHeaderScope.restype = c_int
    PdfixLib.PdeCellSetHeaderScope.argtypes = [c_void_p, c_int]
    PdfixLib.PdeCellGetRowSpan.restype = c_int
    PdfixLib.PdeCellGetRowSpan.argtypes = [c_void_p]
    PdfixLib.PdeCellSetRowSpan.restype = c_int
    PdfixLib.PdeCellSetRowSpan.argtypes = [c_void_p, c_int]
    PdfixLib.PdeCellGetColSpan.restype = c_int
    PdfixLib.PdeCellGetColSpan.argtypes = [c_void_p]
    PdfixLib.PdeCellSetColSpan.restype = c_int
    PdfixLib.PdeCellSetColSpan.argtypes = [c_void_p, c_int]
    PdfixLib.PdeCellHasBorderGraphicState.restype = c_int
    PdfixLib.PdeCellHasBorderGraphicState.argtypes = [c_void_p, c_int]
    PdfixLib.PdeCellGetSpanCell.restype = c_void_p
    PdfixLib.PdeCellGetSpanCell.argtypes = [c_void_p]
    PdfixLib.PdeCellGetNumAssociatedHeaders.restype = c_int
    PdfixLib.PdeCellGetNumAssociatedHeaders.argtypes = [c_void_p]
    PdfixLib.PdeCellGetAssociatedHeader.restype = c_int
    PdfixLib.PdeCellGetAssociatedHeader.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdeCellAddAssociatedHeader.restype = c_int
    PdfixLib.PdeCellAddAssociatedHeader.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdeCellRemoveAssociatedHeader.restype = c_int
    PdfixLib.PdeCellRemoveAssociatedHeader.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTableGetNumRows.restype = c_int
    PdfixLib.PdeTableGetNumRows.argtypes = [c_void_p]
    PdfixLib.PdeTableSetNumRows.restype = c_int
    PdfixLib.PdeTableSetNumRows.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTableGetNumCols.restype = c_int
    PdfixLib.PdeTableGetNumCols.argtypes = [c_void_p]
    PdfixLib.PdeTableSetNumCols.restype = c_int
    PdfixLib.PdeTableSetNumCols.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTableGetCell.restype = c_void_p
    PdfixLib.PdeTableGetCell.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdeTableGetRowAlignment.restype = c_int
    PdfixLib.PdeTableGetRowAlignment.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTableGetColAlignment.restype = c_int
    PdfixLib.PdeTableGetColAlignment.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTableGetCaption.restype = c_void_p
    PdfixLib.PdeTableGetCaption.argtypes = [c_void_p]
    PdfixLib.PdeTableGetTableType.restype = c_int
    PdfixLib.PdeTableGetTableType.argtypes = [c_void_p]
    PdfixLib.PdeTextRunGetTextObject.restype = c_void_p
    PdfixLib.PdeTextRunGetTextObject.argtypes = [c_void_p]
    PdfixLib.PdeTextRunGetFirstCharIndex.restype = c_int
    PdfixLib.PdeTextRunGetFirstCharIndex.argtypes = [c_void_p]
    PdfixLib.PdeTextRunGetLastCharIndex.restype = c_int
    PdfixLib.PdeTextRunGetLastCharIndex.argtypes = [c_void_p]
    PdfixLib.PdeWordGetText.restype = c_int
    PdfixLib.PdeWordGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdeWordHasTextState.restype = c_int
    PdfixLib.PdeWordHasTextState.argtypes = [c_void_p]
    PdfixLib.PdeWordGetTextState.restype = c_int
    PdfixLib.PdeWordGetTextState.argtypes = [c_void_p, POINTER(zz_PdfTextState)]
    PdfixLib.PdeWordGetNumChars.restype = c_int
    PdfixLib.PdeWordGetNumChars.argtypes = [c_void_p, c_int]
    PdfixLib.PdeWordGetCharCode.restype = c_int
    PdfixLib.PdeWordGetCharCode.argtypes = [c_void_p, c_int]
    PdfixLib.PdeWordGetCharText.restype = c_int
    PdfixLib.PdeWordGetCharText.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdeWordGetCharTextState.restype = c_int
    PdfixLib.PdeWordGetCharTextState.argtypes = [c_void_p, c_int, POINTER(zz_PdfTextState)]
    PdfixLib.PdeWordGetCharBBox.restype = c_int
    PdfixLib.PdeWordGetCharBBox.argtypes = [c_void_p, c_int, POINTER(zz_PdfRect)]
    PdfixLib.PdeWordGetWordFlags.restype = c_int
    PdfixLib.PdeWordGetWordFlags.argtypes = [c_void_p]
    PdfixLib.PdeWordGetBackground.restype = c_void_p
    PdfixLib.PdeWordGetBackground.argtypes = [c_void_p]
    PdfixLib.PdeWordGetOrigin.restype = c_int
    PdfixLib.PdeWordGetOrigin.argtypes = [c_void_p, POINTER(zz_PdfPoint)]
    PdfixLib.PdeWordGetNumTextRuns.restype = c_int
    PdfixLib.PdeWordGetNumTextRuns.argtypes = [c_void_p, c_int]
    PdfixLib.PdeWordGetTextRun.restype = c_void_p
    PdfixLib.PdeWordGetTextRun.argtypes = [c_void_p, c_int]
    PdfixLib.PdeWordGetCharStateFlags.restype = c_int
    PdfixLib.PdeWordGetCharStateFlags.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTextLineGetText.restype = c_int
    PdfixLib.PdeTextLineGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdeTextLineHasTextState.restype = c_int
    PdfixLib.PdeTextLineHasTextState.argtypes = [c_void_p]
    PdfixLib.PdeTextLineGetTextState.restype = c_int
    PdfixLib.PdeTextLineGetTextState.argtypes = [c_void_p, POINTER(zz_PdfTextState)]
    PdfixLib.PdeTextLineGetNumWords.restype = c_int
    PdfixLib.PdeTextLineGetNumWords.argtypes = [c_void_p]
    PdfixLib.PdeTextLineGetWord.restype = c_void_p
    PdfixLib.PdeTextLineGetWord.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTextLineGetTextLineFlags.restype = c_int
    PdfixLib.PdeTextLineGetTextLineFlags.argtypes = [c_void_p]
    PdfixLib.PdeTextGetText.restype = c_int
    PdfixLib.PdeTextGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdeTextHasTextState.restype = c_int
    PdfixLib.PdeTextHasTextState.argtypes = [c_void_p]
    PdfixLib.PdeTextGetTextState.restype = c_int
    PdfixLib.PdeTextGetTextState.argtypes = [c_void_p, POINTER(zz_PdfTextState)]
    PdfixLib.PdeTextGetNumTextLines.restype = c_int
    PdfixLib.PdeTextGetNumTextLines.argtypes = [c_void_p]
    PdfixLib.PdeTextGetTextLine.restype = c_void_p
    PdfixLib.PdeTextGetTextLine.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTextGetNumWords.restype = c_int
    PdfixLib.PdeTextGetNumWords.argtypes = [c_void_p]
    PdfixLib.PdeTextGetWord.restype = c_void_p
    PdfixLib.PdeTextGetWord.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTextGetLineSpacing.restype = c_float
    PdfixLib.PdeTextGetLineSpacing.argtypes = [c_void_p]
    PdfixLib.PdeTextGetIndent.restype = c_float
    PdfixLib.PdeTextGetIndent.argtypes = [c_void_p]
    PdfixLib.PdeTextGetTextStyle.restype = c_int
    PdfixLib.PdeTextGetTextStyle.argtypes = [c_void_p]
    PdfixLib.PdeTextSetTextStyle.restype = c_int
    PdfixLib.PdeTextSetTextStyle.argtypes = [c_void_p, c_int]
    PdfixLib.PdeTextGetTextFlags.restype = c_int
    PdfixLib.PdeTextGetTextFlags.argtypes = [c_void_p]
    PdfixLib.PdeTextSetTextFlags.restype = c_int
    PdfixLib.PdeTextSetTextFlags.argtypes = [c_void_p, c_int]
    PdfixLib.PdfColorSpaceGetName.restype = c_int
    PdfixLib.PdfColorSpaceGetName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfColorSpaceGetFamilyType.restype = c_int
    PdfixLib.PdfColorSpaceGetFamilyType.argtypes = [c_void_p]
    PdfixLib.PdfColorSpaceGetNumComps.restype = c_int
    PdfixLib.PdfColorSpaceGetNumComps.argtypes = [c_void_p]
    PdfixLib.PdfColorSpaceCreateColor.restype = c_void_p
    PdfixLib.PdfColorSpaceCreateColor.argtypes = [c_void_p]
    PdfixLib.PdfColorGetColorSpace.restype = c_void_p
    PdfixLib.PdfColorGetColorSpace.argtypes = [c_void_p]
    PdfixLib.PdfColorSetColorSpace.restype = c_int
    PdfixLib.PdfColorSetColorSpace.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfColorGetValue.restype = c_float
    PdfixLib.PdfColorGetValue.argtypes = [c_void_p, c_int]
    PdfixLib.PdfColorSetValue.restype = c_int
    PdfixLib.PdfColorSetValue.argtypes = [c_void_p, c_int, c_float]
    PdfixLib.PdfColorGetRGB.restype = c_int
    PdfixLib.PdfColorGetRGB.argtypes = [c_void_p, POINTER(zz_PdfRGB)]
    PdfixLib.PdfColorGetCMYK.restype = c_int
    PdfixLib.PdfColorGetCMYK.argtypes = [c_void_p, POINTER(zz_PdfCMYK)]
    PdfixLib.PdfColorGetGrayscale.restype = c_int
    PdfixLib.PdfColorGetGrayscale.argtypes = [c_void_p, POINTER(zz_PdfGray)]
    PdfixLib.PdfColorDestroy.restype = c_int
    PdfixLib.PdfColorDestroy.argtypes = [c_void_p]
    PdfixLib.PdfActionGetSubtype.restype = c_int
    PdfixLib.PdfActionGetSubtype.argtypes = [c_void_p]
    PdfixLib.PdfActionGetJavaScript.restype = c_int
    PdfixLib.PdfActionGetJavaScript.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfActionGetObject.restype = c_void_p
    PdfixLib.PdfActionGetObject.argtypes = [c_void_p]
    PdfixLib.PdfActionGetDestFile.restype = c_int
    PdfixLib.PdfActionGetDestFile.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfActionGetViewDestination.restype = c_void_p
    PdfixLib.PdfActionGetViewDestination.argtypes = [c_void_p]
    PdfixLib.PdfActionSetViewDestination.restype = c_int
    PdfixLib.PdfActionSetViewDestination.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfActionCanCopy.restype = c_int
    PdfixLib.PdfActionCanCopy.argtypes = [c_void_p]
    PdfixLib.PdfActionCanPaste.restype = c_int
    PdfixLib.PdfActionCanPaste.argtypes = [c_void_p, c_void_p, c_void_p]
    PdfixLib.PdfActionCopy.restype = c_void_p
    PdfixLib.PdfActionCopy.argtypes = [c_void_p]
    PdfixLib.PdfActionPaste.restype = c_void_p
    PdfixLib.PdfActionPaste.argtypes = [c_void_p, c_void_p, c_void_p]
    PdfixLib.PdfActionDestroyClipboardData.restype = c_int
    PdfixLib.PdfActionDestroyClipboardData.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfActionGetNumChildren.restype = c_int
    PdfixLib.PdfActionGetNumChildren.argtypes = [c_void_p]
    PdfixLib.PdfActionGetChild.restype = c_void_p
    PdfixLib.PdfActionGetChild.argtypes = [c_void_p, c_int]
    PdfixLib.PdfActionRemoveChild.restype = c_int
    PdfixLib.PdfActionRemoveChild.argtypes = [c_void_p, c_int]
    PdfixLib.PdfActionHandlerGetType.restype = c_int
    PdfixLib.PdfActionHandlerGetType.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfActionHandlerDestroy.restype = c_int
    PdfixLib.PdfActionHandlerDestroy.argtypes = [c_void_p]
    PdfixLib.PdfActionHandlerSetCanCopyProc.restype = c_int
    PdfixLib.PdfActionHandlerSetCanCopyProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfActionHandlerSetCopyProc.restype = c_int
    PdfixLib.PdfActionHandlerSetCopyProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfActionHandlerSetCanPasteProc.restype = c_int
    PdfixLib.PdfActionHandlerSetCanPasteProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfActionHandlerSetPasteProc.restype = c_int
    PdfixLib.PdfActionHandlerSetPasteProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfActionHandlerSetDestroyDataProc.restype = c_int
    PdfixLib.PdfActionHandlerSetDestroyDataProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfActionHandlerSetDestroyProc.restype = c_int
    PdfixLib.PdfActionHandlerSetDestroyProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfAnnotGetSubtype.restype = c_int
    PdfixLib.PdfAnnotGetSubtype.argtypes = [c_void_p]
    PdfixLib.PdfAnnotGetFlags.restype = c_int
    PdfixLib.PdfAnnotGetFlags.argtypes = [c_void_p]
    PdfixLib.PdfAnnotSetFlags.restype = c_int
    PdfixLib.PdfAnnotSetFlags.argtypes = [c_void_p, c_int]
    PdfixLib.PdfAnnotGetAppearance.restype = c_int
    PdfixLib.PdfAnnotGetAppearance.argtypes = [c_void_p, POINTER(zz_PdfAnnotAppearance)]
    PdfixLib.PdfAnnotGetAppearanceXObject.restype = c_void_p
    PdfixLib.PdfAnnotGetAppearanceXObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdfAnnotSetAppearanceFromXObject.restype = c_int
    PdfixLib.PdfAnnotSetAppearanceFromXObject.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdfAnnotRefreshAppearance.restype = c_int
    PdfixLib.PdfAnnotRefreshAppearance.argtypes = [c_void_p]
    PdfixLib.PdfAnnotGetBBox.restype = c_int
    PdfixLib.PdfAnnotGetBBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfAnnotPointInAnnot.restype = c_int
    PdfixLib.PdfAnnotPointInAnnot.argtypes = [c_void_p, POINTER(zz_PdfPoint)]
    PdfixLib.PdfAnnotRectInAnnot.restype = c_int
    PdfixLib.PdfAnnotRectInAnnot.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfAnnotGetStructObject.restype = c_void_p
    PdfixLib.PdfAnnotGetStructObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdfAnnotGetObject.restype = c_void_p
    PdfixLib.PdfAnnotGetObject.argtypes = [c_void_p]
    PdfixLib.PdfAnnotNotifyWillChange.restype = c_int
    PdfixLib.PdfAnnotNotifyWillChange.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfAnnotNotifyDidChange.restype = c_int
    PdfixLib.PdfAnnotNotifyDidChange.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfAnnotIsValid.restype = c_int
    PdfixLib.PdfAnnotIsValid.argtypes = [c_void_p]
    PdfixLib.PdfAnnotIsMarkup.restype = c_int
    PdfixLib.PdfAnnotIsMarkup.argtypes = [c_void_p]
    PdfixLib.PdfAnnotCanCopy.restype = c_int
    PdfixLib.PdfAnnotCanCopy.argtypes = [c_void_p]
    PdfixLib.PdfAnnotCanPaste.restype = c_int
    PdfixLib.PdfAnnotCanPaste.argtypes = [c_void_p, c_void_p, POINTER(zz_PdfPoint), c_void_p]
    PdfixLib.PdfAnnotCopy.restype = c_void_p
    PdfixLib.PdfAnnotCopy.argtypes = [c_void_p]
    PdfixLib.PdfAnnotPaste.restype = c_void_p
    PdfixLib.PdfAnnotPaste.argtypes = [c_void_p, c_void_p, POINTER(zz_PdfPoint), c_void_p]
    PdfixLib.PdfAnnotDestroyClipboardData.restype = c_int
    PdfixLib.PdfAnnotDestroyClipboardData.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfAnnotGetStateFlags.restype = c_int
    PdfixLib.PdfAnnotGetStateFlags.argtypes = [c_void_p]
    PdfixLib.PdfAnnotSetStateFlags.restype = c_int
    PdfixLib.PdfAnnotSetStateFlags.argtypes = [c_void_p, c_int]
    PdfixLib.PdfAnnotGetPageObject.restype = c_void_p
    PdfixLib.PdfAnnotGetPageObject.argtypes = [c_void_p]
    PdfixLib.PdfLinkAnnotGetNumQuads.restype = c_int
    PdfixLib.PdfLinkAnnotGetNumQuads.argtypes = [c_void_p]
    PdfixLib.PdfLinkAnnotGetQuad.restype = c_int
    PdfixLib.PdfLinkAnnotGetQuad.argtypes = [c_void_p, c_int, POINTER(zz_PdfQuad)]
    PdfixLib.PdfLinkAnnotAddQuad.restype = c_int
    PdfixLib.PdfLinkAnnotAddQuad.argtypes = [c_void_p, POINTER(zz_PdfQuad)]
    PdfixLib.PdfLinkAnnotRemoveQuad.restype = c_int
    PdfixLib.PdfLinkAnnotRemoveQuad.argtypes = [c_void_p, c_int]
    PdfixLib.PdfLinkAnnotGetAction.restype = c_void_p
    PdfixLib.PdfLinkAnnotGetAction.argtypes = [c_void_p]
    PdfixLib.PdfLinkAnnotSetAction.restype = c_int
    PdfixLib.PdfLinkAnnotSetAction.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfMarkupAnnotGetContents.restype = c_int
    PdfixLib.PdfMarkupAnnotGetContents.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfMarkupAnnotSetContents.restype = c_int
    PdfixLib.PdfMarkupAnnotSetContents.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfMarkupAnnotGetAuthor.restype = c_int
    PdfixLib.PdfMarkupAnnotGetAuthor.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfMarkupAnnotSetAuthor.restype = c_int
    PdfixLib.PdfMarkupAnnotSetAuthor.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfMarkupAnnotGetNumReplies.restype = c_int
    PdfixLib.PdfMarkupAnnotGetNumReplies.argtypes = [c_void_p]
    PdfixLib.PdfMarkupAnnotGetReply.restype = c_void_p
    PdfixLib.PdfMarkupAnnotGetReply.argtypes = [c_void_p, c_int]
    PdfixLib.PdfMarkupAnnotAddReply.restype = c_void_p
    PdfixLib.PdfMarkupAnnotAddReply.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfTextMarkupAnnotGetNumQuads.restype = c_int
    PdfixLib.PdfTextMarkupAnnotGetNumQuads.argtypes = [c_void_p]
    PdfixLib.PdfTextMarkupAnnotGetQuad.restype = c_int
    PdfixLib.PdfTextMarkupAnnotGetQuad.argtypes = [c_void_p, c_int, POINTER(zz_PdfQuad)]
    PdfixLib.PdfTextMarkupAnnotAddQuad.restype = c_int
    PdfixLib.PdfTextMarkupAnnotAddQuad.argtypes = [c_void_p, POINTER(zz_PdfQuad)]
    PdfixLib.PdfTextMarkupAnnotRemoveQuad.restype = c_int
    PdfixLib.PdfTextMarkupAnnotRemoveQuad.argtypes = [c_void_p, c_int]
    PdfixLib.PdfWidgetAnnotGetCaption.restype = c_int
    PdfixLib.PdfWidgetAnnotGetCaption.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfWidgetAnnotGetFontName.restype = c_int
    PdfixLib.PdfWidgetAnnotGetFontName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfWidgetAnnotGetAction.restype = c_void_p
    PdfixLib.PdfWidgetAnnotGetAction.argtypes = [c_void_p]
    PdfixLib.PdfWidgetAnnotSetAction.restype = c_int
    PdfixLib.PdfWidgetAnnotSetAction.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfWidgetAnnotGetAAction.restype = c_void_p
    PdfixLib.PdfWidgetAnnotGetAAction.argtypes = [c_void_p, c_int]
    PdfixLib.PdfWidgetAnnotGetFormField.restype = c_void_p
    PdfixLib.PdfWidgetAnnotGetFormField.argtypes = [c_void_p]
    PdfixLib.PdfAnnotHandlerGetType.restype = c_int
    PdfixLib.PdfAnnotHandlerGetType.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfAnnotHandlerDestroy.restype = c_int
    PdfixLib.PdfAnnotHandlerDestroy.argtypes = [c_void_p]
    PdfixLib.PdfAnnotHandlerSetCanCopyProc.restype = c_int
    PdfixLib.PdfAnnotHandlerSetCanCopyProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfAnnotHandlerSetCopyProc.restype = c_int
    PdfixLib.PdfAnnotHandlerSetCopyProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfAnnotHandlerSetCanPasteProc.restype = c_int
    PdfixLib.PdfAnnotHandlerSetCanPasteProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfAnnotHandlerSetPasteProc.restype = c_int
    PdfixLib.PdfAnnotHandlerSetPasteProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfAnnotHandlerSetDestroyDataProc.restype = c_int
    PdfixLib.PdfAnnotHandlerSetDestroyDataProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfAnnotHandlerSetDestroyProc.restype = c_int
    PdfixLib.PdfAnnotHandlerSetDestroyProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfViewDestinationGetPageNum.restype = c_int
    PdfixLib.PdfViewDestinationGetPageNum.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfViewDestinationGetFitType.restype = c_int
    PdfixLib.PdfViewDestinationGetFitType.argtypes = [c_void_p]
    PdfixLib.PdfViewDestinationGetBBox.restype = c_int
    PdfixLib.PdfViewDestinationGetBBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfViewDestinationGetZoom.restype = c_float
    PdfixLib.PdfViewDestinationGetZoom.argtypes = [c_void_p]
    PdfixLib.PdfViewDestinationGetObject.restype = c_void_p
    PdfixLib.PdfViewDestinationGetObject.argtypes = [c_void_p]
    PdfixLib.PdfSecurityHandlerGetFilter.restype = c_int
    PdfixLib.PdfSecurityHandlerGetFilter.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfSecurityHandlerDestroy.restype = c_int
    PdfixLib.PdfSecurityHandlerDestroy.argtypes = [c_void_p]
    PdfixLib.PdfStandardSecurityHandlerSetPassword.restype = c_int
    PdfixLib.PdfStandardSecurityHandlerSetPassword.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfStandardSecurityHandlerHasPassword.restype = c_int
    PdfixLib.PdfStandardSecurityHandlerHasPassword.argtypes = [c_void_p, c_int]
    PdfixLib.PdfStandardSecurityHandlerGetParams.restype = c_int
    PdfixLib.PdfStandardSecurityHandlerGetParams.argtypes = [c_void_p, POINTER(zz_PdfStandardSecurityParams)]
    PdfixLib.PdfCustomSecurityHandlerSetAuthorizationData.restype = c_int
    PdfixLib.PdfCustomSecurityHandlerSetAuthorizationData.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfCustomSecurityHandlerSetDestroyProc.restype = c_int
    PdfixLib.PdfCustomSecurityHandlerSetDestroyProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfCustomSecurityHandlerSetSetAuthoziationDataProc.restype = c_int
    PdfixLib.PdfCustomSecurityHandlerSetSetAuthoziationDataProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfCustomSecurityHandlerSetOnInitProc.restype = c_int
    PdfixLib.PdfCustomSecurityHandlerSetOnInitProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfCustomSecurityHandlerSetGetPermissionsProc.restype = c_int
    PdfixLib.PdfCustomSecurityHandlerSetGetPermissionsProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfCustomSecurityHandlerSetIsMetadataEncryptedProc.restype = c_int
    PdfixLib.PdfCustomSecurityHandlerSetIsMetadataEncryptedProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfCustomSecurityHandlerSetUpdateEncryptDictProc.restype = c_int
    PdfixLib.PdfCustomSecurityHandlerSetUpdateEncryptDictProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfCustomSecurityHandlerSetAuthorizeOwnerProc.restype = c_int
    PdfixLib.PdfCustomSecurityHandlerSetAuthorizeOwnerProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfCustomSecurityHandlerSetGetDecryptSizeProc.restype = c_int
    PdfixLib.PdfCustomSecurityHandlerSetGetDecryptSizeProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfCustomSecurityHandlerSetDecryptContentProc.restype = c_int
    PdfixLib.PdfCustomSecurityHandlerSetDecryptContentProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfCustomSecurityHandlerSetGetEncryptSizeProc.restype = c_int
    PdfixLib.PdfCustomSecurityHandlerSetGetEncryptSizeProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfCustomSecurityHandlerSetEncryptContentProc.restype = c_int
    PdfixLib.PdfCustomSecurityHandlerSetEncryptContentProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdfBaseDigSigDestroy.restype = c_int
    PdfixLib.PdfBaseDigSigDestroy.argtypes = [c_void_p]
    PdfixLib.PdfBaseDigSigSetReason.restype = c_int
    PdfixLib.PdfBaseDigSigSetReason.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfBaseDigSigSetLocation.restype = c_int
    PdfixLib.PdfBaseDigSigSetLocation.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfBaseDigSigSetContactInfo.restype = c_int
    PdfixLib.PdfBaseDigSigSetContactInfo.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfBaseDigSigSetName.restype = c_int
    PdfixLib.PdfBaseDigSigSetName.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfBaseDigSigSetTimeStampServer.restype = c_int
    PdfixLib.PdfBaseDigSigSetTimeStampServer.argtypes = [c_void_p, c_wchar_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfBaseDigSigSignDoc.restype = c_int
    PdfixLib.PdfBaseDigSigSignDoc.argtypes = [c_void_p, c_void_p, c_wchar_p]
    PdfixLib.PdfDigSigSetPfxFile.restype = c_int
    PdfixLib.PdfDigSigSetPfxFile.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfCustomDigSigRegisterDigestDataProc.restype = c_int
    PdfixLib.PdfCustomDigSigRegisterDigestDataProc.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PdfDocUndoBeginOperation.restype = c_int
    PdfixLib.PdfDocUndoBeginOperation.argtypes = [c_void_p]
    PdfixLib.PdfDocUndoEndOperation.restype = c_int
    PdfixLib.PdfDocUndoEndOperation.argtypes = [c_void_p]
    PdfixLib.PdfDocUndoGetNumEntries.restype = c_int
    PdfixLib.PdfDocUndoGetNumEntries.argtypes = [c_void_p]
    PdfixLib.PdfDocUndoExecute.restype = c_int
    PdfixLib.PdfDocUndoExecute.argtypes = [c_void_p]
    PdfixLib.PdfDocUndoGetTitle.restype = c_int
    PdfixLib.PdfDocUndoGetTitle.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfDocUndoGetData.restype = c_void_p
    PdfixLib.PdfDocUndoGetData.argtypes = [c_void_p]
    PdfixLib.PdfDocSave.restype = c_int
    PdfixLib.PdfDocSave.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfDocSaveToStream.restype = c_int
    PdfixLib.PdfDocSaveToStream.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdfDocClose.restype = c_int
    PdfixLib.PdfDocClose.argtypes = [c_void_p]
    PdfixLib.PdfDocAuthorize.restype = c_int
    PdfixLib.PdfDocAuthorize.argtypes = [c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdfDocIsSecured.restype = c_int
    PdfixLib.PdfDocIsSecured.argtypes = [c_void_p]
    PdfixLib.PdfDocSetSecurityHandler.restype = c_int
    PdfixLib.PdfDocSetSecurityHandler.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfDocGetSecurityHandler.restype = c_void_p
    PdfixLib.PdfDocGetSecurityHandler.argtypes = [c_void_p]
    PdfixLib.PdfDocGetNumPages.restype = c_int
    PdfixLib.PdfDocGetNumPages.argtypes = [c_void_p]
    PdfixLib.PdfDocAcquirePage.restype = c_void_p
    PdfixLib.PdfDocAcquirePage.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocCreatePage.restype = c_void_p
    PdfixLib.PdfDocCreatePage.argtypes = [c_void_p, c_int, POINTER(zz_PdfRect)]
    PdfixLib.PdfDocDeletePages.restype = c_int
    PdfixLib.PdfDocDeletePages.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdfDocInsertPages.restype = c_int
    PdfixLib.PdfDocInsertPages.argtypes = [c_void_p, c_int, c_void_p, c_int, c_int, c_int]
    PdfixLib.PdfDocMovePage.restype = c_int
    PdfixLib.PdfDocMovePage.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdfDocGetNumDocumentJavaScripts.restype = c_int
    PdfixLib.PdfDocGetNumDocumentJavaScripts.argtypes = [c_void_p]
    PdfixLib.PdfDocGetDocumentJavaScript.restype = c_int
    PdfixLib.PdfDocGetDocumentJavaScript.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdfDocGetDocumentJavaScriptName.restype = c_int
    PdfixLib.PdfDocGetDocumentJavaScriptName.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdfDocGetNumCalculatedFormFields.restype = c_int
    PdfixLib.PdfDocGetNumCalculatedFormFields.argtypes = [c_void_p]
    PdfixLib.PdfDocGetCalculatedFormField.restype = c_void_p
    PdfixLib.PdfDocGetCalculatedFormField.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocGetNumFormFields.restype = c_int
    PdfixLib.PdfDocGetNumFormFields.argtypes = [c_void_p]
    PdfixLib.PdfDocGetFormField.restype = c_void_p
    PdfixLib.PdfDocGetFormField.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocGetFormFieldByName.restype = c_void_p
    PdfixLib.PdfDocGetFormFieldByName.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfDocGetInfo.restype = c_int
    PdfixLib.PdfDocGetInfo.argtypes = [c_void_p, c_wchar_p, c_wchar_p, c_int]
    PdfixLib.PdfDocSetInfo.restype = c_int
    PdfixLib.PdfDocSetInfo.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfDocGetBookmarkRoot.restype = c_void_p
    PdfixLib.PdfDocGetBookmarkRoot.argtypes = [c_void_p]
    PdfixLib.PdfDocCreateBookmarkRoot.restype = c_void_p
    PdfixLib.PdfDocCreateBookmarkRoot.argtypes = [c_void_p]
    PdfixLib.PdfDocApplyRedaction.restype = c_int
    PdfixLib.PdfDocApplyRedaction.argtypes = [c_void_p]
    PdfixLib.PdfDocGetNumAlternates.restype = c_int
    PdfixLib.PdfDocGetNumAlternates.argtypes = [c_void_p]
    PdfixLib.PdfDocAcquireAlternate.restype = c_void_p
    PdfixLib.PdfDocAcquireAlternate.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocAddTags.restype = c_int
    PdfixLib.PdfDocAddTags.argtypes = [c_void_p, POINTER(zz_PdfTagsParams)]
    PdfixLib.PdfDocRemoveTags.restype = c_int
    PdfixLib.PdfDocRemoveTags.argtypes = [c_void_p]
    PdfixLib.PdfDocGetTemplate.restype = c_void_p
    PdfixLib.PdfDocGetTemplate.argtypes = [c_void_p]
    PdfixLib.PdfDocGetMetadata.restype = c_void_p
    PdfixLib.PdfDocGetMetadata.argtypes = [c_void_p]
    PdfixLib.PdfDocGetLang.restype = c_int
    PdfixLib.PdfDocGetLang.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfDocSetLang.restype = c_int
    PdfixLib.PdfDocSetLang.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfDocReplaceFont.restype = c_int
    PdfixLib.PdfDocReplaceFont.argtypes = [c_void_p, c_void_p, c_wchar_p]
    PdfixLib.PdfDocEmbedFont.restype = c_int
    PdfixLib.PdfDocEmbedFont.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdfDocEmbedFonts.restype = c_int
    PdfixLib.PdfDocEmbedFonts.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocGetTrailerObject.restype = c_void_p
    PdfixLib.PdfDocGetTrailerObject.argtypes = [c_void_p]
    PdfixLib.PdfDocGetRootObject.restype = c_void_p
    PdfixLib.PdfDocGetRootObject.argtypes = [c_void_p]
    PdfixLib.PdfDocGetInfoObject.restype = c_void_p
    PdfixLib.PdfDocGetInfoObject.argtypes = [c_void_p]
    PdfixLib.PdfDocCreateDictObject.restype = c_void_p
    PdfixLib.PdfDocCreateDictObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocCreateArrayObject.restype = c_void_p
    PdfixLib.PdfDocCreateArrayObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocCreateBooleanObject.restype = c_void_p
    PdfixLib.PdfDocCreateBooleanObject.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdfDocCreateNameObject.restype = c_void_p
    PdfixLib.PdfDocCreateNameObject.argtypes = [c_void_p, c_int, c_wchar_p]
    PdfixLib.PdfDocCreateStringObject.restype = c_void_p
    PdfixLib.PdfDocCreateStringObject.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdfDocCreateIntObject.restype = c_void_p
    PdfixLib.PdfDocCreateIntObject.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdfDocCreateNumberObject.restype = c_void_p
    PdfixLib.PdfDocCreateNumberObject.argtypes = [c_void_p, c_int, c_float]
    PdfixLib.PdfDocCreateStreamObject.restype = c_void_p
    PdfixLib.PdfDocCreateStreamObject.argtypes = [c_void_p, c_int, c_void_p, POINTER(c_ubyte), c_int]
    PdfixLib.PdfDocCreateXObjectFromImage.restype = c_void_p
    PdfixLib.PdfDocCreateXObjectFromImage.argtypes = [c_void_p, c_void_p, c_int, c_int]
    PdfixLib.PdfDocCreateXObjectFromPage.restype = c_void_p
    PdfixLib.PdfDocCreateXObjectFromPage.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfDocGetObjectById.restype = c_void_p
    PdfixLib.PdfDocGetObjectById.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocCreateStructTree.restype = c_void_p
    PdfixLib.PdfDocCreateStructTree.argtypes = [c_void_p]
    PdfixLib.PdfDocGetStructTree.restype = c_void_p
    PdfixLib.PdfDocGetStructTree.argtypes = [c_void_p]
    PdfixLib.PdfDocRemoveStructTree.restype = c_int
    PdfixLib.PdfDocRemoveStructTree.argtypes = [c_void_p]
    PdfixLib.PdfDocRemoveBookmarks.restype = c_int
    PdfixLib.PdfDocRemoveBookmarks.argtypes = [c_void_p]
    PdfixLib.PdfDocCreateBookmarks.restype = c_int
    PdfixLib.PdfDocCreateBookmarks.argtypes = [c_void_p]
    PdfixLib.PdfDocAddFontMissingUnicode.restype = c_int
    PdfixLib.PdfDocAddFontMissingUnicode.argtypes = [c_void_p]
    PdfixLib.PdfDocGetNameTree.restype = c_void_p
    PdfixLib.PdfDocGetNameTree.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfDocRemoveNameTree.restype = c_int
    PdfixLib.PdfDocRemoveNameTree.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfDocGetPageNumFromObject.restype = c_int
    PdfixLib.PdfDocGetPageNumFromObject.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfDocGetAnnotFromObject.restype = c_void_p
    PdfixLib.PdfDocGetAnnotFromObject.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfDocGetBookmarkFromObject.restype = c_void_p
    PdfixLib.PdfDocGetBookmarkFromObject.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfDocGetActionFromObject.restype = c_void_p
    PdfixLib.PdfDocGetActionFromObject.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfDocGetActionFromViewDest.restype = c_void_p
    PdfixLib.PdfDocGetActionFromViewDest.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfDocGetViewDestinationFromObject.restype = c_void_p
    PdfixLib.PdfDocGetViewDestinationFromObject.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfDocCreateViewDestination.restype = c_void_p
    PdfixLib.PdfDocCreateViewDestination.argtypes = [c_void_p, c_int, c_int, POINTER(zz_PdfRect), c_float]
    PdfixLib.PdfDocCreateFormFromObject.restype = c_void_p
    PdfixLib.PdfDocCreateFormFromObject.argtypes = [c_void_p, c_void_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdfDocCreateAction.restype = c_void_p
    PdfixLib.PdfDocCreateAction.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocCreateContent.restype = c_void_p
    PdfixLib.PdfDocCreateContent.argtypes = [c_void_p]
    PdfixLib.PdfDocCreateColorSpace.restype = c_void_p
    PdfixLib.PdfDocCreateColorSpace.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocCreateFont.restype = c_void_p
    PdfixLib.PdfDocCreateFont.argtypes = [c_void_p, c_void_p, c_int, c_int]
    PdfixLib.PdfDocCreateUndo.restype = c_void_p
    PdfixLib.PdfDocCreateUndo.argtypes = [c_void_p, c_wchar_p, c_void_p]
    PdfixLib.PdfDocGetNumUndos.restype = c_int
    PdfixLib.PdfDocGetNumUndos.argtypes = [c_void_p]
    PdfixLib.PdfDocGetUndo.restype = c_void_p
    PdfixLib.PdfDocGetUndo.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocClearUndos.restype = c_int
    PdfixLib.PdfDocClearUndos.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocGetNumRedos.restype = c_int
    PdfixLib.PdfDocGetNumRedos.argtypes = [c_void_p]
    PdfixLib.PdfDocGetRedo.restype = c_void_p
    PdfixLib.PdfDocGetRedo.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocClearRedos.restype = c_int
    PdfixLib.PdfDocClearRedos.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocGetFlags.restype = c_int
    PdfixLib.PdfDocGetFlags.argtypes = [c_void_p]
    PdfixLib.PdfDocSetFlags.restype = c_int
    PdfixLib.PdfDocSetFlags.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocClearFlags.restype = c_int
    PdfixLib.PdfDocClearFlags.argtypes = [c_void_p]
    PdfixLib.PdfDocGetUserPermissions.restype = c_int
    PdfixLib.PdfDocGetUserPermissions.argtypes = [c_void_p]
    PdfixLib.PdfDocGetVersion.restype = c_int
    PdfixLib.PdfDocGetVersion.argtypes = [c_void_p]
    PdfixLib.PdfDocSetVersion.restype = c_int
    PdfixLib.PdfDocSetVersion.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocGetPdfStandard.restype = c_int
    PdfixLib.PdfDocGetPdfStandard.argtypes = [c_void_p]
    PdfixLib.PdfDocSetPdfStandard.restype = c_int
    PdfixLib.PdfDocSetPdfStandard.argtypes = [c_void_p, c_int, c_wchar_p]
    PdfixLib.PdfDocGetPath.restype = c_int
    PdfixLib.PdfDocGetPath.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfDocSetPath.restype = c_int
    PdfixLib.PdfDocSetPath.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfDocCreateHtmlConversion.restype = c_void_p
    PdfixLib.PdfDocCreateHtmlConversion.argtypes = [c_void_p]
    PdfixLib.PdfDocCreateJsonConversion.restype = c_void_p
    PdfixLib.PdfDocCreateJsonConversion.argtypes = [c_void_p]
    PdfixLib.PdfDocCreateTiffConversion.restype = c_void_p
    PdfixLib.PdfDocCreateTiffConversion.argtypes = [c_void_p]
    PdfixLib.PdfDocGetCommand.restype = c_void_p
    PdfixLib.PdfDocGetCommand.argtypes = [c_void_p]
    PdfixLib.PdfDocEnumFonts.restype = c_int
    PdfixLib.PdfDocEnumFonts.argtypes = [c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdfDocEnumBookmarks.restype = c_int
    PdfixLib.PdfDocEnumBookmarks.argtypes = [c_void_p, c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdfDocEnumAnnots.restype = c_int
    PdfixLib.PdfDocEnumAnnots.argtypes = [c_void_p, c_int, c_int, c_int, c_void_p]
    PdfixLib.PdfDocEnumPageObjects.restype = c_int
    PdfixLib.PdfDocEnumPageObjects.argtypes = [c_void_p, c_void_p, c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdfDocEnumStructTree.restype = c_int
    PdfixLib.PdfDocEnumStructTree.argtypes = [c_void_p, c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdfDocGetProgressControl.restype = c_void_p
    PdfixLib.PdfDocGetProgressControl.argtypes = [c_void_p]
    PdfixLib.PdfDocCreateFileSpec.restype = c_void_p
    PdfixLib.PdfDocCreateFileSpec.argtypes = [c_void_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, POINTER(c_ubyte), c_int]
    PdfixLib.PdsFileSpecGetDictionary.restype = c_void_p
    PdfixLib.PdsFileSpecGetDictionary.argtypes = [c_void_p]
    PdfixLib.PdsFileSpecGetFileName.restype = c_int
    PdfixLib.PdsFileSpecGetFileName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsFileSpecSetFileName.restype = c_int
    PdfixLib.PdsFileSpecSetFileName.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsFileSpecGetFileStm.restype = c_void_p
    PdfixLib.PdsFileSpecGetFileStm.argtypes = [c_void_p]
    PdfixLib.PdfDocTemplateUpdate.restype = c_int
    PdfixLib.PdfDocTemplateUpdate.argtypes = [c_void_p]
    PdfixLib.PdfDocTemplateLoadFromStream.restype = c_int
    PdfixLib.PdfDocTemplateLoadFromStream.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdfDocTemplateSaveToStream.restype = c_int
    PdfixLib.PdfDocTemplateSaveToStream.argtypes = [c_void_p, c_void_p, c_int, c_int]
    PdfixLib.PdfDocTemplateSetDefaults.restype = c_int
    PdfixLib.PdfDocTemplateSetDefaults.argtypes = [c_void_p]
    PdfixLib.PdfDocTemplateGetProperty.restype = c_float
    PdfixLib.PdfDocTemplateGetProperty.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfDocTemplateSetProperty.restype = c_int
    PdfixLib.PdfDocTemplateSetProperty.argtypes = [c_void_p, c_wchar_p, c_float]
    PdfixLib.PdfDocTemplateGetRegex.restype = c_int
    PdfixLib.PdfDocTemplateGetRegex.argtypes = [c_void_p, c_wchar_p, c_wchar_p, c_int]
    PdfixLib.PdfDocTemplateSetRegex.restype = c_int
    PdfixLib.PdfDocTemplateSetRegex.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfDocTemplateAddPage.restype = c_int
    PdfixLib.PdfDocTemplateAddPage.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocTemplateGetPageTemplate.restype = c_void_p
    PdfixLib.PdfDocTemplateGetPageTemplate.argtypes = [c_void_p, c_int]
    PdfixLib.PdfDocTemplateGetNumNodes.restype = c_int
    PdfixLib.PdfDocTemplateGetNumNodes.argtypes = [c_void_p, c_int, c_char_p]
    PdfixLib.PdfDocTemplateGetNodeBBox.restype = c_int
    PdfixLib.PdfDocTemplateGetNodeBBox.argtypes = [c_void_p, c_int, c_char_p, c_int, POINTER(zz_PdfRect)]
    PdfixLib.PdfDocTemplateGetVersionMajor.restype = c_int
    PdfixLib.PdfDocTemplateGetVersionMajor.argtypes = [c_void_p]
    PdfixLib.PdfDocTemplateGetVersionMinor.restype = c_int
    PdfixLib.PdfDocTemplateGetVersionMinor.argtypes = [c_void_p]
    PdfixLib.PdfPageTemplateGetPageNum.restype = c_int
    PdfixLib.PdfPageTemplateGetPageNum.argtypes = [c_void_p]
    PdfixLib.PdfPageTemplateGetLogicalRotate.restype = c_int
    PdfixLib.PdfPageTemplateGetLogicalRotate.argtypes = [c_void_p]
    PdfixLib.PdfPageTemplateGetNumColumns.restype = c_int
    PdfixLib.PdfPageTemplateGetNumColumns.argtypes = [c_void_p]
    PdfixLib.PdfPageTemplateGetHeaderBBox.restype = c_int
    PdfixLib.PdfPageTemplateGetHeaderBBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfPageTemplateGetFooterBBox.restype = c_int
    PdfixLib.PdfPageTemplateGetFooterBBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfAlternateGetSubtype.restype = c_int
    PdfixLib.PdfAlternateGetSubtype.argtypes = [c_void_p]
    PdfixLib.PdfAlternateGetName.restype = c_int
    PdfixLib.PdfAlternateGetName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfAlternateGetDescription.restype = c_int
    PdfixLib.PdfAlternateGetDescription.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfAlternateGetFileName.restype = c_int
    PdfixLib.PdfAlternateGetFileName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfAlternateSaveContent.restype = c_int
    PdfixLib.PdfAlternateSaveContent.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfAlternateRelease.restype = c_int
    PdfixLib.PdfAlternateRelease.argtypes = [c_void_p]
    PdfixLib.PdfHtmlAlternateSaveResource.restype = c_int
    PdfixLib.PdfHtmlAlternateSaveResource.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfFontGetFontName.restype = c_int
    PdfixLib.PdfFontGetFontName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFontGetFaceName.restype = c_int
    PdfixLib.PdfFontGetFaceName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFontGetFontState.restype = c_int
    PdfixLib.PdfFontGetFontState.argtypes = [c_void_p, POINTER(zz_PdfFontState)]
    PdfixLib.PdfFontGetSystemFontName.restype = c_int
    PdfixLib.PdfFontGetSystemFontName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFontGetSystemFontCharset.restype = c_int
    PdfixLib.PdfFontGetSystemFontCharset.argtypes = [c_void_p]
    PdfixLib.PdfFontGetSystemFontBold.restype = c_int
    PdfixLib.PdfFontGetSystemFontBold.argtypes = [c_void_p]
    PdfixLib.PdfFontGetSystemFontItalic.restype = c_int
    PdfixLib.PdfFontGetSystemFontItalic.argtypes = [c_void_p]
    PdfixLib.PdfFontSaveToStream.restype = c_int
    PdfixLib.PdfFontSaveToStream.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdfFontGetEmbedded.restype = c_int
    PdfixLib.PdfFontGetEmbedded.argtypes = [c_void_p]
    PdfixLib.PdfFontGetUnicodeFromCharcode.restype = c_int
    PdfixLib.PdfFontGetUnicodeFromCharcode.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdfFontSetUnicodeForCharcode.restype = c_int
    PdfixLib.PdfFontSetUnicodeForCharcode.argtypes = [c_void_p, c_int, c_wchar_p]
    PdfixLib.PdfFontGetObject.restype = c_void_p
    PdfixLib.PdfFontGetObject.argtypes = [c_void_p]
    PdfixLib.PdfFormFieldGetType.restype = c_int
    PdfixLib.PdfFormFieldGetType.argtypes = [c_void_p]
    PdfixLib.PdfFormFieldGetFlags.restype = c_int
    PdfixLib.PdfFormFieldGetFlags.argtypes = [c_void_p]
    PdfixLib.PdfFormFieldSetFlags.restype = c_int
    PdfixLib.PdfFormFieldSetFlags.argtypes = [c_void_p, c_int]
    PdfixLib.PdfFormFieldGetValue.restype = c_int
    PdfixLib.PdfFormFieldGetValue.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldSetValue.restype = c_int
    PdfixLib.PdfFormFieldSetValue.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfFormFieldGetDefaultValue.restype = c_int
    PdfixLib.PdfFormFieldGetDefaultValue.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldGetFullName.restype = c_int
    PdfixLib.PdfFormFieldGetFullName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldGetTooltip.restype = c_int
    PdfixLib.PdfFormFieldGetTooltip.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldGetNumOptions.restype = c_int
    PdfixLib.PdfFormFieldGetNumOptions.argtypes = [c_void_p]
    PdfixLib.PdfFormFieldGetOptionValue.restype = c_int
    PdfixLib.PdfFormFieldGetOptionValue.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldGetOptionCaption.restype = c_int
    PdfixLib.PdfFormFieldGetOptionCaption.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldGetAction.restype = c_void_p
    PdfixLib.PdfFormFieldGetAction.argtypes = [c_void_p]
    PdfixLib.PdfFormFieldGetAAction.restype = c_void_p
    PdfixLib.PdfFormFieldGetAAction.argtypes = [c_void_p, c_int]
    PdfixLib.PdfFormFieldGetMaxLength.restype = c_int
    PdfixLib.PdfFormFieldGetMaxLength.argtypes = [c_void_p]
    PdfixLib.PdfFormFieldGetWidgetExportValue.restype = c_int
    PdfixLib.PdfFormFieldGetWidgetExportValue.argtypes = [c_void_p, c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldGetObject.restype = c_void_p
    PdfixLib.PdfFormFieldGetObject.argtypes = [c_void_p]
    PdfixLib.PdfFormFieldGetNumExportValues.restype = c_int
    PdfixLib.PdfFormFieldGetNumExportValues.argtypes = [c_void_p]
    PdfixLib.PdfFormFieldGetExportValue.restype = c_int
    PdfixLib.PdfFormFieldGetExportValue.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdfFormFieldNotifyWillChange.restype = c_int
    PdfixLib.PdfFormFieldNotifyWillChange.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfFormFieldNotifyDidChange.restype = c_int
    PdfixLib.PdfFormFieldNotifyDidChange.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfPageRelease.restype = c_int
    PdfixLib.PdfPageRelease.argtypes = [c_void_p]
    PdfixLib.PdfPageGetRefNum.restype = c_int
    PdfixLib.PdfPageGetRefNum.argtypes = [c_void_p]
    PdfixLib.PdfPageGetCropBox.restype = c_int
    PdfixLib.PdfPageGetCropBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfPageGetMediaBox.restype = c_int
    PdfixLib.PdfPageGetMediaBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfPageGetRotate.restype = c_int
    PdfixLib.PdfPageGetRotate.argtypes = [c_void_p]
    PdfixLib.PdfPageSetRotate.restype = c_int
    PdfixLib.PdfPageSetRotate.argtypes = [c_void_p, c_int]
    PdfixLib.PdfPageGetLogicalRotate.restype = c_int
    PdfixLib.PdfPageGetLogicalRotate.argtypes = [c_void_p]
    PdfixLib.PdfPageGetDefaultMatrix.restype = c_int
    PdfixLib.PdfPageGetDefaultMatrix.argtypes = [c_void_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdfPageGetTemplateMatrix.restype = c_int
    PdfixLib.PdfPageGetTemplateMatrix.argtypes = [c_void_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdfPageGetNumber.restype = c_int
    PdfixLib.PdfPageGetNumber.argtypes = [c_void_p]
    PdfixLib.PdfPageAcquirePageMap.restype = c_void_p
    PdfixLib.PdfPageAcquirePageMap.argtypes = [c_void_p]
    PdfixLib.PdfPageAcquirePageView.restype = c_void_p
    PdfixLib.PdfPageAcquirePageView.argtypes = [c_void_p, c_float, c_int]
    PdfixLib.PdfPageGetNumAnnots.restype = c_int
    PdfixLib.PdfPageGetNumAnnots.argtypes = [c_void_p]
    PdfixLib.PdfPageGetAnnot.restype = c_void_p
    PdfixLib.PdfPageGetAnnot.argtypes = [c_void_p, c_int]
    PdfixLib.PdfPageRemoveAnnot.restype = c_int
    PdfixLib.PdfPageRemoveAnnot.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdfPageAddAnnot.restype = c_int
    PdfixLib.PdfPageAddAnnot.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PdfPageCreateAnnot.restype = c_void_p
    PdfixLib.PdfPageCreateAnnot.argtypes = [c_void_p, c_int, POINTER(zz_PdfRect)]
    PdfixLib.PdfPageGetNumAnnotsAtPoint.restype = c_int
    PdfixLib.PdfPageGetNumAnnotsAtPoint.argtypes = [c_void_p, POINTER(zz_PdfPoint)]
    PdfixLib.PdfPageGetAnnotAtPoint.restype = c_void_p
    PdfixLib.PdfPageGetAnnotAtPoint.argtypes = [c_void_p, POINTER(zz_PdfPoint), c_int]
    PdfixLib.PdfPageGetNumAnnotsAtRect.restype = c_int
    PdfixLib.PdfPageGetNumAnnotsAtRect.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdfPageGetAnnotAtRect.restype = c_void_p
    PdfixLib.PdfPageGetAnnotAtRect.argtypes = [c_void_p, POINTER(zz_PdfRect), c_int]
    PdfixLib.PdfPageDrawContent.restype = c_int
    PdfixLib.PdfPageDrawContent.argtypes = [c_void_p, POINTER(zz_PdfPageRenderParams)]
    PdfixLib.PdfPageGetContent.restype = c_void_p
    PdfixLib.PdfPageGetContent.argtypes = [c_void_p]
    PdfixLib.PdfPageGetResources.restype = c_void_p
    PdfixLib.PdfPageGetResources.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfPageGetObject.restype = c_void_p
    PdfixLib.PdfPageGetObject.argtypes = [c_void_p]
    PdfixLib.PdfPageFlattenFormXObjects.restype = c_int
    PdfixLib.PdfPageFlattenFormXObjects.argtypes = [c_void_p]
    PdfixLib.PdfPageCloneFormXObjects.restype = c_int
    PdfixLib.PdfPageCloneFormXObjects.argtypes = [c_void_p]
    PdfixLib.PdfPageFlattenAnnot.restype = c_int
    PdfixLib.PdfPageFlattenAnnot.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfPageGetContentFlags.restype = c_int
    PdfixLib.PdfPageGetContentFlags.argtypes = [c_void_p]
    PdfixLib.PdfPageSetContent.restype = c_int
    PdfixLib.PdfPageSetContent.argtypes = [c_void_p]
    PdfixLib.PdfPageGetDoc.restype = c_void_p
    PdfixLib.PdfPageGetDoc.argtypes = [c_void_p]
    PdfixLib.PdfPageAcquireWordList.restype = c_void_p
    PdfixLib.PdfPageAcquireWordList.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdfPageGetFlags.restype = c_int
    PdfixLib.PdfPageGetFlags.argtypes = [c_void_p]
    PdfixLib.PdfPageSetFlags.restype = c_int
    PdfixLib.PdfPageSetFlags.argtypes = [c_void_p, c_int]
    PdfixLib.PdfPageClearFlags.restype = c_int
    PdfixLib.PdfPageClearFlags.argtypes = [c_void_p]
    PdfixLib.PdfPageCreateFormFromObject.restype = c_void_p
    PdfixLib.PdfPageCreateFormFromObject.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdePageMapRelease.restype = c_int
    PdfixLib.PdePageMapRelease.argtypes = [c_void_p]
    PdfixLib.PdePageMapGetElement.restype = c_void_p
    PdfixLib.PdePageMapGetElement.argtypes = [c_void_p]
    PdfixLib.PdePageMapGetWhitespace.restype = c_int
    PdfixLib.PdePageMapGetWhitespace.argtypes = [c_void_p, POINTER(zz_PdfWhitespaceParams), c_int, POINTER(zz_PdfRect)]
    PdfixLib.PdePageMapGetBBox.restype = c_int
    PdfixLib.PdePageMapGetBBox.argtypes = [c_void_p, POINTER(zz_PdfRect)]
    PdfixLib.PdePageMapHasElements.restype = c_int
    PdfixLib.PdePageMapHasElements.argtypes = [c_void_p]
    PdfixLib.PdePageMapCreateElements.restype = c_int
    PdfixLib.PdePageMapCreateElements.argtypes = [c_void_p]
    PdfixLib.PdePageMapRemoveElements.restype = c_int
    PdfixLib.PdePageMapRemoveElements.argtypes = [c_void_p]
    PdfixLib.PdePageMapCreateElement.restype = c_void_p
    PdfixLib.PdePageMapCreateElement.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PdePageMapAddTags.restype = c_int
    PdfixLib.PdePageMapAddTags.argtypes = [c_void_p, c_void_p, c_int, POINTER(zz_PdfTagsParams)]
    PdfixLib.PdePageMapGetPage.restype = c_void_p
    PdfixLib.PdePageMapGetPage.argtypes = [c_void_p]
    PdfixLib.PdePageMapGetNumArtifacts.restype = c_int
    PdfixLib.PdePageMapGetNumArtifacts.argtypes = [c_void_p]
    PdfixLib.PdePageMapGetArtifact.restype = c_void_p
    PdfixLib.PdePageMapGetArtifact.argtypes = [c_void_p, c_int]
    PdfixLib.PdfPageViewRelease.restype = c_int
    PdfixLib.PdfPageViewRelease.argtypes = [c_void_p]
    PdfixLib.PdfPageViewGetDeviceWidth.restype = c_int
    PdfixLib.PdfPageViewGetDeviceWidth.argtypes = [c_void_p]
    PdfixLib.PdfPageViewGetDeviceHeight.restype = c_int
    PdfixLib.PdfPageViewGetDeviceHeight.argtypes = [c_void_p]
    PdfixLib.PdfPageViewGetDeviceMatrix.restype = c_int
    PdfixLib.PdfPageViewGetDeviceMatrix.argtypes = [c_void_p, POINTER(zz_PdfMatrix)]
    PdfixLib.PdfPageViewRectToDevice.restype = c_int
    PdfixLib.PdfPageViewRectToDevice.argtypes = [c_void_p, POINTER(zz_PdfRect), POINTER(zz_PdfDevRect)]
    PdfixLib.PdfPageViewPointToDevice.restype = c_int
    PdfixLib.PdfPageViewPointToDevice.argtypes = [c_void_p, POINTER(zz_PdfPoint), POINTER(zz_PdfDevPoint)]
    PdfixLib.PdfPageViewRectToPage.restype = c_int
    PdfixLib.PdfPageViewRectToPage.argtypes = [c_void_p, POINTER(zz_PdfDevRect), POINTER(zz_PdfRect)]
    PdfixLib.PdfPageViewPointToPage.restype = c_int
    PdfixLib.PdfPageViewPointToPage.argtypes = [c_void_p, POINTER(zz_PdfDevPoint), POINTER(zz_PdfPoint)]
    PdfixLib.PdfBookmarkGetTitle.restype = c_int
    PdfixLib.PdfBookmarkGetTitle.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfBookmarkSetTitle.restype = c_int
    PdfixLib.PdfBookmarkSetTitle.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfBookmarkGetAppearance.restype = c_int
    PdfixLib.PdfBookmarkGetAppearance.argtypes = [c_void_p, POINTER(zz_PdfBookmarkAppearance)]
    PdfixLib.PdfBookmarkSetAppearance.restype = c_int
    PdfixLib.PdfBookmarkSetAppearance.argtypes = [c_void_p, POINTER(zz_PdfBookmarkAppearance)]
    PdfixLib.PdfBookmarkGetAction.restype = c_void_p
    PdfixLib.PdfBookmarkGetAction.argtypes = [c_void_p]
    PdfixLib.PdfBookmarkSetAction.restype = c_int
    PdfixLib.PdfBookmarkSetAction.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfBookmarkGetNumChildren.restype = c_int
    PdfixLib.PdfBookmarkGetNumChildren.argtypes = [c_void_p]
    PdfixLib.PdfBookmarkGetChild.restype = c_void_p
    PdfixLib.PdfBookmarkGetChild.argtypes = [c_void_p, c_int]
    PdfixLib.PdfBookmarkGetParent.restype = c_void_p
    PdfixLib.PdfBookmarkGetParent.argtypes = [c_void_p]
    PdfixLib.PdfBookmarkGetNext.restype = c_void_p
    PdfixLib.PdfBookmarkGetNext.argtypes = [c_void_p]
    PdfixLib.PdfBookmarkGetPrev.restype = c_void_p
    PdfixLib.PdfBookmarkGetPrev.argtypes = [c_void_p]
    PdfixLib.PdfBookmarkGetObject.restype = c_void_p
    PdfixLib.PdfBookmarkGetObject.argtypes = [c_void_p]
    PdfixLib.PdfBookmarkAddChild.restype = c_int
    PdfixLib.PdfBookmarkAddChild.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PdfBookmarkAddNewChild.restype = c_void_p
    PdfixLib.PdfBookmarkAddNewChild.argtypes = [c_void_p, c_int, c_wchar_p]
    PdfixLib.PdfBookmarkIsValid.restype = c_int
    PdfixLib.PdfBookmarkIsValid.argtypes = [c_void_p]
    PdfixLib.PdfBookmarkRemoveChild.restype = c_void_p
    PdfixLib.PdfBookmarkRemoveChild.argtypes = [c_void_p, c_int]
    PdfixLib.PdfBookmarkIsOpen.restype = c_int
    PdfixLib.PdfBookmarkIsOpen.argtypes = [c_void_p]
    PdfixLib.PdfBookmarkSetOpen.restype = c_int
    PdfixLib.PdfBookmarkSetOpen.argtypes = [c_void_p, c_int]
    PdfixLib.PdfNameTreeGetObject.restype = c_void_p
    PdfixLib.PdfNameTreeGetObject.argtypes = [c_void_p]
    PdfixLib.PdfNameTreeLookup.restype = c_void_p
    PdfixLib.PdfNameTreeLookup.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PsRegexDestroy.restype = c_int
    PdfixLib.PsRegexDestroy.argtypes = [c_void_p]
    PdfixLib.PsRegexSetPattern.restype = c_int
    PdfixLib.PsRegexSetPattern.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PsRegexSearch.restype = c_int
    PdfixLib.PsRegexSearch.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PsRegexGetText.restype = c_int
    PdfixLib.PsRegexGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PsRegexGetPosition.restype = c_int
    PdfixLib.PsRegexGetPosition.argtypes = [c_void_p]
    PdfixLib.PsRegexGetLength.restype = c_int
    PdfixLib.PsRegexGetLength.argtypes = [c_void_p]
    PdfixLib.PsRegexGetNumMatches.restype = c_int
    PdfixLib.PsRegexGetNumMatches.argtypes = [c_void_p]
    PdfixLib.PsRegexGetMatchText.restype = c_int
    PdfixLib.PsRegexGetMatchText.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PsStreamDestroy.restype = c_int
    PdfixLib.PsStreamDestroy.argtypes = [c_void_p]
    PdfixLib.PsStreamIsEof.restype = c_int
    PdfixLib.PsStreamIsEof.argtypes = [c_void_p]
    PdfixLib.PsStreamGetSize.restype = c_int
    PdfixLib.PsStreamGetSize.argtypes = [c_void_p]
    PdfixLib.PsStreamRead.restype = c_int
    PdfixLib.PsStreamRead.argtypes = [c_void_p, c_int, POINTER(c_ubyte), c_int]
    PdfixLib.PsStreamWrite.restype = c_int
    PdfixLib.PsStreamWrite.argtypes = [c_void_p, c_int, POINTER(c_ubyte), c_int]
    PdfixLib.PsStreamGetPos.restype = c_int
    PdfixLib.PsStreamGetPos.argtypes = [c_void_p]
    PdfixLib.PsStreamFlush.restype = c_int
    PdfixLib.PsStreamFlush.argtypes = [c_void_p]
    PdfixLib.PsStreamGetStream.restype = c_void_p
    PdfixLib.PsStreamGetStream.argtypes = [c_void_p]
    PdfixLib.PsStreamGetType.restype = c_int
    PdfixLib.PsStreamGetType.argtypes = [c_void_p]
    PdfixLib.PsMemoryStreamResize.restype = c_int
    PdfixLib.PsMemoryStreamResize.argtypes = [c_void_p, c_int]
    PdfixLib.PsCustomStreamSetReadProc.restype = c_int
    PdfixLib.PsCustomStreamSetReadProc.argtypes = [c_void_p, c_int]
    PdfixLib.PsCustomStreamSetWriteProc.restype = c_int
    PdfixLib.PsCustomStreamSetWriteProc.argtypes = [c_void_p, c_int]
    PdfixLib.PsCustomStreamSetDestroyProc.restype = c_int
    PdfixLib.PsCustomStreamSetDestroyProc.argtypes = [c_void_p, c_int]
    PdfixLib.PsCustomStreamSetGetSizeProc.restype = c_int
    PdfixLib.PsCustomStreamSetGetSizeProc.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementGetType.restype = c_int
    PdfixLib.PdsStructElementGetType.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdsStructElementSetType.restype = c_int
    PdfixLib.PdsStructElementSetType.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsStructElementGetActualText.restype = c_int
    PdfixLib.PdsStructElementGetActualText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStructElementSetActualText.restype = c_int
    PdfixLib.PdsStructElementSetActualText.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsStructElementGetAlt.restype = c_int
    PdfixLib.PdsStructElementGetAlt.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStructElementSetAlt.restype = c_int
    PdfixLib.PdsStructElementSetAlt.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsStructElementGetTitle.restype = c_int
    PdfixLib.PdsStructElementGetTitle.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStructElementSetTitle.restype = c_int
    PdfixLib.PdsStructElementSetTitle.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsStructElementGetText.restype = c_int
    PdfixLib.PdsStructElementGetText.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdsStructElementGetAbbreviation.restype = c_int
    PdfixLib.PdsStructElementGetAbbreviation.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStructElementGetNumPages.restype = c_int
    PdfixLib.PdsStructElementGetNumPages.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetPageNumber.restype = c_int
    PdfixLib.PdsStructElementGetPageNumber.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementGetBBox.restype = c_int
    PdfixLib.PdsStructElementGetBBox.argtypes = [c_void_p, c_int, POINTER(zz_PdfRect)]
    PdfixLib.PdsStructElementGetAttrObject.restype = c_void_p
    PdfixLib.PdsStructElementGetAttrObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementAddAttrObj.restype = c_int
    PdfixLib.PdsStructElementAddAttrObj.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdsStructElementRemoveAttrObj.restype = c_int
    PdfixLib.PdsStructElementRemoveAttrObj.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetObject.restype = c_void_p
    PdfixLib.PdsStructElementGetObject.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetChildObject.restype = c_void_p
    PdfixLib.PdsStructElementGetChildObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementGetChildType.restype = c_int
    PdfixLib.PdsStructElementGetChildType.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementGetChildPageNumber.restype = c_int
    PdfixLib.PdsStructElementGetChildPageNumber.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementGetChildMcid.restype = c_int
    PdfixLib.PdsStructElementGetChildMcid.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementGetNumAttrObjects.restype = c_int
    PdfixLib.PdsStructElementGetNumAttrObjects.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetNumChildren.restype = c_int
    PdfixLib.PdsStructElementGetNumChildren.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetParentObject.restype = c_void_p
    PdfixLib.PdsStructElementGetParentObject.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetId.restype = c_int
    PdfixLib.PdsStructElementGetId.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStructElementSetId.restype = c_int
    PdfixLib.PdsStructElementSetId.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsStructElementGetLang.restype = c_int
    PdfixLib.PdsStructElementGetLang.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStructElementSetLang.restype = c_int
    PdfixLib.PdsStructElementSetLang.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsStructElementRemoveChild.restype = c_int
    PdfixLib.PdsStructElementRemoveChild.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementMoveChild.restype = c_int
    PdfixLib.PdsStructElementMoveChild.argtypes = [c_void_p, c_int, c_void_p, c_int]
    PdfixLib.PdsStructElementAddChild.restype = c_int
    PdfixLib.PdsStructElementAddChild.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdsStructElementAddNewChild.restype = c_void_p
    PdfixLib.PdsStructElementAddNewChild.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStructElementAddPageObject.restype = c_int
    PdfixLib.PdsStructElementAddPageObject.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdsStructElementAddAnnot.restype = c_void_p
    PdfixLib.PdsStructElementAddAnnot.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdsStructElementGetStructTree.restype = c_void_p
    PdfixLib.PdsStructElementGetStructTree.argtypes = [c_void_p]
    PdfixLib.PdsStructElementRecognizeTable.restype = c_int
    PdfixLib.PdsStructElementRecognizeTable.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetNumRow.restype = c_int
    PdfixLib.PdsStructElementGetNumRow.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetNumCol.restype = c_int
    PdfixLib.PdsStructElementGetNumCol.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetCell.restype = c_void_p
    PdfixLib.PdsStructElementGetCell.argtypes = [c_void_p, c_int, c_int]
    PdfixLib.PdsStructElementGetCellParams.restype = c_int
    PdfixLib.PdsStructElementGetCellParams.argtypes = [c_void_p, c_int, c_int, POINTER(zz_PdfCellParams)]
    PdfixLib.PdsStructElementGetCellElemParams.restype = c_int
    PdfixLib.PdsStructElementGetCellElemParams.argtypes = [c_void_p, c_void_p, POINTER(zz_PdfCellParams)]
    PdfixLib.PdsStructElementGetNumAssociatedHeaders.restype = c_int
    PdfixLib.PdsStructElementGetNumAssociatedHeaders.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetAssociatedHeader.restype = c_void_p
    PdfixLib.PdsStructElementGetAssociatedHeader.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementAddAssociatedHeader.restype = c_int
    PdfixLib.PdsStructElementAddAssociatedHeader.argtypes = [c_void_p, c_int, c_void_p, c_int]
    PdfixLib.PdsStructElementRemoveAssociatedHeader.restype = c_int
    PdfixLib.PdsStructElementRemoveAssociatedHeader.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementAddAssociatedFile.restype = c_int
    PdfixLib.PdsStructElementAddAssociatedFile.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdsStructElementGetNumAssociatedFiles.restype = c_int
    PdfixLib.PdsStructElementGetNumAssociatedFiles.argtypes = [c_void_p]
    PdfixLib.PdsStructElementGetAssociatedFile.restype = c_void_p
    PdfixLib.PdsStructElementGetAssociatedFile.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructElementValidChild.restype = c_int
    PdfixLib.PdsStructElementValidChild.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PdsClassMapGetAttrObject.restype = c_void_p
    PdfixLib.PdsClassMapGetAttrObject.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsClassMapGetNumAttrObjects.restype = c_int
    PdfixLib.PdsClassMapGetNumAttrObjects.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdsClassMapGetObject.restype = c_void_p
    PdfixLib.PdsClassMapGetObject.argtypes = [c_void_p]
    PdfixLib.PdsRoleMapDoesMap.restype = c_int
    PdfixLib.PdsRoleMapDoesMap.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdsRoleMapGetDirectMap.restype = c_int
    PdfixLib.PdsRoleMapGetDirectMap.argtypes = [c_void_p, c_wchar_p, c_wchar_p, c_int]
    PdfixLib.PdsRoleMapGetObject.restype = c_void_p
    PdfixLib.PdsRoleMapGetObject.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeGetObject.restype = c_void_p
    PdfixLib.PdsStructTreeGetObject.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeGetClassMap.restype = c_void_p
    PdfixLib.PdsStructTreeGetClassMap.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeCreateClassMap.restype = c_void_p
    PdfixLib.PdsStructTreeCreateClassMap.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeRemoveClassMap.restype = c_int
    PdfixLib.PdsStructTreeRemoveClassMap.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeGetChildObject.restype = c_void_p
    PdfixLib.PdsStructTreeGetChildObject.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructTreeGetNumChildren.restype = c_int
    PdfixLib.PdsStructTreeGetNumChildren.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeGetRoleMap.restype = c_void_p
    PdfixLib.PdsStructTreeGetRoleMap.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeCreateRoleMap.restype = c_void_p
    PdfixLib.PdsStructTreeCreateRoleMap.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeRemoveRoleMap.restype = c_int
    PdfixLib.PdsStructTreeRemoveRoleMap.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeGetStructElementFromObject.restype = c_void_p
    PdfixLib.PdsStructTreeGetStructElementFromObject.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdsStructTreeRemoveChild.restype = c_int
    PdfixLib.PdsStructTreeRemoveChild.argtypes = [c_void_p, c_int]
    PdfixLib.PdsStructTreeAddChild.restype = c_int
    PdfixLib.PdsStructTreeAddChild.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdsStructTreeAddNewChild.restype = c_void_p
    PdfixLib.PdsStructTreeAddNewChild.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdsStructTreeGetDoc.restype = c_void_p
    PdfixLib.PdsStructTreeGetDoc.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeFixParentTree.restype = c_int
    PdfixLib.PdsStructTreeFixParentTree.argtypes = [c_void_p]
    PdfixLib.PdsStructTreeFixIdTree.restype = c_int
    PdfixLib.PdsStructTreeFixIdTree.argtypes = [c_void_p]
    PdfixLib.PdfConversionDestroy.restype = c_int
    PdfixLib.PdfConversionDestroy.argtypes = [c_void_p]
    PdfixLib.PdfConversionAddPage.restype = c_int
    PdfixLib.PdfConversionAddPage.argtypes = [c_void_p, c_int]
    PdfixLib.PdfConversionSave.restype = c_int
    PdfixLib.PdfConversionSave.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfConversionSaveToStream.restype = c_int
    PdfixLib.PdfConversionSaveToStream.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfHtmlConversionSetParams.restype = c_int
    PdfixLib.PdfHtmlConversionSetParams.argtypes = [c_void_p, POINTER(zz_PdfHtmlParams)]
    PdfixLib.PdfHtmlConversionSaveCSS.restype = c_int
    PdfixLib.PdfHtmlConversionSaveCSS.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfHtmlConversionSaveJavaScript.restype = c_int
    PdfixLib.PdfHtmlConversionSaveJavaScript.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfHtmlConversionAddHtml.restype = c_int
    PdfixLib.PdfHtmlConversionAddHtml.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfJsonConversionSetParams.restype = c_int
    PdfixLib.PdfJsonConversionSetParams.argtypes = [c_void_p, POINTER(zz_PdfJsonParams)]
    PdfixLib.PdfTiffConversionSetParams.restype = c_int
    PdfixLib.PdfTiffConversionSetParams.argtypes = [c_void_p, POINTER(zz_PdfTiffParams)]
    PdfixLib.PdfSelectionEnumPageObjects.restype = c_int
    PdfixLib.PdfSelectionEnumPageObjects.argtypes = [c_void_p, c_int, c_void_p, c_int]
    PdfixLib.PdfSelectionEnumPages.restype = c_int
    PdfixLib.PdfSelectionEnumPages.argtypes = [c_void_p, c_int, c_void_p, c_int]
    PdfixLib.PdfSelectionEnumStructElements.restype = c_int
    PdfixLib.PdfSelectionEnumStructElements.argtypes = [c_void_p, c_int, c_void_p, c_int]
    PdfixLib.PdfSelectionEnumAnnots.restype = c_int
    PdfixLib.PdfSelectionEnumAnnots.argtypes = [c_void_p, c_int, c_void_p, c_int]
    PdfixLib.PdfSelectionEnumFonts.restype = c_int
    PdfixLib.PdfSelectionEnumFonts.argtypes = [c_void_p, c_int, c_void_p, c_int]
    PdfixLib.PsEventGetType.restype = c_int
    PdfixLib.PsEventGetType.argtypes = [c_void_p]
    PdfixLib.PsEventGetDoc.restype = c_void_p
    PdfixLib.PsEventGetDoc.argtypes = [c_void_p]
    PdfixLib.PsEventGetPage.restype = c_void_p
    PdfixLib.PsEventGetPage.argtypes = [c_void_p]
    PdfixLib.PsEventGetObject.restype = c_void_p
    PdfixLib.PsEventGetObject.argtypes = [c_void_p]
    PdfixLib.PsEventGetFormField.restype = c_void_p
    PdfixLib.PsEventGetFormField.argtypes = [c_void_p]
    PdfixLib.PsEventGetProgressControl.restype = c_void_p
    PdfixLib.PsEventGetProgressControl.argtypes = [c_void_p]
    PdfixLib.PsEventGetUndo.restype = c_void_p
    PdfixLib.PsEventGetUndo.argtypes = [c_void_p]
    PdfixLib.PsEventGetName.restype = c_int
    PdfixLib.PsEventGetName.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PsEventGetIndex.restype = c_int
    PdfixLib.PsEventGetIndex.argtypes = [c_void_p]
    PdfixLib.PsAuthorizationSaveToStream.restype = c_int
    PdfixLib.PsAuthorizationSaveToStream.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PsAuthorizationIsAuthorized.restype = c_int
    PdfixLib.PsAuthorizationIsAuthorized.argtypes = [c_void_p]
    PdfixLib.PsAuthorizationIsAuthorizedPlatform.restype = c_int
    PdfixLib.PsAuthorizationIsAuthorizedPlatform.argtypes = [c_void_p, c_int]
    PdfixLib.PsAuthorizationIsAuthorizedOption.restype = c_int
    PdfixLib.PsAuthorizationIsAuthorizedOption.argtypes = [c_void_p, c_int]
    PdfixLib.PsAuthorizationGetType.restype = c_int
    PdfixLib.PsAuthorizationGetType.argtypes = [c_void_p]
    PdfixLib.PsAccountAuthorizationAuthorize.restype = c_int
    PdfixLib.PsAccountAuthorizationAuthorize.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PsAccountAuthorizationReset.restype = c_int
    PdfixLib.PsAccountAuthorizationReset.argtypes = [c_void_p]
    PdfixLib.PsStandardAuthorizationActivate.restype = c_int
    PdfixLib.PsStandardAuthorizationActivate.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PsStandardAuthorizationCreateOfflineActivationFile.restype = c_int
    PdfixLib.PsStandardAuthorizationCreateOfflineActivationFile.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PsStandardAuthorizationActivateOffline.restype = c_int
    PdfixLib.PsStandardAuthorizationActivateOffline.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PsStandardAuthorizationDeactivate.restype = c_int
    PdfixLib.PsStandardAuthorizationDeactivate.argtypes = [c_void_p]
    PdfixLib.PsStandardAuthorizationDeactivateOffline.restype = c_int
    PdfixLib.PsStandardAuthorizationDeactivateOffline.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PsStandardAuthorizationUpdate.restype = c_int
    PdfixLib.PsStandardAuthorizationUpdate.argtypes = [c_void_p, c_int]
    PdfixLib.PsStandardAuthorizationUpdateOffline.restype = c_int
    PdfixLib.PsStandardAuthorizationUpdateOffline.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PsStandardAuthorizationReset.restype = c_int
    PdfixLib.PsStandardAuthorizationReset.argtypes = [c_void_p]
    PdfixLib.PsCommandLoadParamsFromStream.restype = c_int
    PdfixLib.PsCommandLoadParamsFromStream.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PsCommandReset.restype = c_int
    PdfixLib.PsCommandReset.argtypes = [c_void_p]
    PdfixLib.PsCommandSaveOutputToStream.restype = c_int
    PdfixLib.PsCommandSaveOutputToStream.argtypes = [c_void_p, c_void_p, c_int, c_int]
    PdfixLib.PsCommandSaveCommandsToStream.restype = c_int
    PdfixLib.PsCommandSaveCommandsToStream.argtypes = [c_void_p, c_int, c_void_p, c_int, c_int]
    PdfixLib.PsCommandSetSelection.restype = c_int
    PdfixLib.PsCommandSetSelection.argtypes = [c_void_p, c_void_p]
    PdfixLib.PsCommandRun.restype = c_int
    PdfixLib.PsCommandRun.argtypes = [c_void_p]
    PdfixLib.PsProgressControlSetCancelProc.restype = c_int
    PdfixLib.PsProgressControlSetCancelProc.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PsProgressControlSetData.restype = c_int
    PdfixLib.PsProgressControlSetData.argtypes = [c_void_p, c_void_p]
    PdfixLib.PsProgressControlGetData.restype = c_void_p
    PdfixLib.PsProgressControlGetData.argtypes = [c_void_p]
    PdfixLib.PsProgressControlStartProcess.restype = c_int
    PdfixLib.PsProgressControlStartProcess.argtypes = [c_void_p, c_int]
    PdfixLib.PsProgressControlEndProcess.restype = c_int
    PdfixLib.PsProgressControlEndProcess.argtypes = [c_void_p, c_int]
    PdfixLib.PsProgressControlStep.restype = c_int
    PdfixLib.PsProgressControlStep.argtypes = [c_void_p, c_int]
    PdfixLib.PsProgressControlSetText.restype = c_int
    PdfixLib.PsProgressControlSetText.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PsProgressControlGetText.restype = c_int
    PdfixLib.PsProgressControlGetText.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PsProgressControlGetState.restype = c_float
    PdfixLib.PsProgressControlGetState.argtypes = [c_void_p]
    PdfixLib.PsProgressControlCancel.restype = c_int
    PdfixLib.PsProgressControlCancel.argtypes = [c_void_p]
    PdfixLib.PsRenderDeviceContextGetType.restype = c_int
    PdfixLib.PsRenderDeviceContextGetType.argtypes = [c_void_p]
    PdfixLib.PsImageDestroy.restype = c_int
    PdfixLib.PsImageDestroy.argtypes = [c_void_p]
    PdfixLib.PsImageSave.restype = c_int
    PdfixLib.PsImageSave.argtypes = [c_void_p, c_wchar_p, POINTER(zz_PdfImageParams)]
    PdfixLib.PsImageSaveRect.restype = c_int
    PdfixLib.PsImageSaveRect.argtypes = [c_void_p, c_wchar_p, POINTER(zz_PdfImageParams), POINTER(zz_PdfDevRect)]
    PdfixLib.PsImageSaveToStream.restype = c_int
    PdfixLib.PsImageSaveToStream.argtypes = [c_void_p, c_void_p, POINTER(zz_PdfImageParams)]
    PdfixLib.PsImageSaveRectToStream.restype = c_int
    PdfixLib.PsImageSaveRectToStream.argtypes = [c_void_p, c_void_p, POINTER(zz_PdfImageParams), POINTER(zz_PdfDevRect)]
    PdfixLib.PsImageGetPointColor.restype = c_int
    PdfixLib.PsImageGetPointColor.argtypes = [c_void_p, POINTER(zz_PdfDevPoint), POINTER(zz_PdfRGB)]
    PdfixLib.PsImageSaveDataToStream.restype = c_int
    PdfixLib.PsImageSaveDataToStream.argtypes = [c_void_p, c_void_p]
    PdfixLib.PsSysFontDestroy.restype = c_int
    PdfixLib.PsSysFontDestroy.argtypes = [c_void_p]
    PdfixLib.PdfixDestroy.restype = c_int
    PdfixLib.PdfixDestroy.argtypes = [c_void_p]
    PdfixLib.PdfixGetAuthorization.restype = c_void_p
    PdfixLib.PdfixGetAuthorization.argtypes = [c_void_p]
    PdfixLib.PdfixGetStandardAuthorization.restype = c_void_p
    PdfixLib.PdfixGetStandardAuthorization.argtypes = [c_void_p]
    PdfixLib.PdfixGetAccountAuthorization.restype = c_void_p
    PdfixLib.PdfixGetAccountAuthorization.argtypes = [c_void_p]
    PdfixLib.PdfixGetErrorType.restype = c_int
    PdfixLib.PdfixGetErrorType.argtypes = [c_void_p]
    PdfixLib.PdfixGetError.restype = c_char_p
    PdfixLib.PdfixGetError.argtypes = [c_void_p]
    PdfixLib.PdfixGetErrorDescription.restype = c_char_p
    PdfixLib.PdfixGetErrorDescription.argtypes = [c_void_p]
    PdfixLib.PdfixSetError.restype = c_int
    PdfixLib.PdfixSetError.argtypes = [c_void_p, c_int, c_char_p, c_char_p]
    PdfixLib.PdfixGetProductName.restype = c_char_p
    PdfixLib.PdfixGetProductName.argtypes = [c_void_p]
    PdfixLib.PdfixGetProductUrl.restype = c_char_p
    PdfixLib.PdfixGetProductUrl.argtypes = [c_void_p]
    PdfixLib.PdfixGetVersionMajor.restype = c_int
    PdfixLib.PdfixGetVersionMajor.argtypes = [c_void_p]
    PdfixLib.PdfixGetVersionMinor.restype = c_int
    PdfixLib.PdfixGetVersionMinor.argtypes = [c_void_p]
    PdfixLib.PdfixGetVersionPatch.restype = c_int
    PdfixLib.PdfixGetVersionPatch.argtypes = [c_void_p]
    PdfixLib.PdfixCreateDoc.restype = c_void_p
    PdfixLib.PdfixCreateDoc.argtypes = [c_void_p]
    PdfixLib.PdfixOpenDoc.restype = c_void_p
    PdfixLib.PdfixOpenDoc.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
    PdfixLib.PdfixOpenDocFromStream.restype = c_void_p
    PdfixLib.PdfixOpenDocFromStream.argtypes = [c_void_p, c_void_p, c_wchar_p]
    PdfixLib.PdfixCreateDigSig.restype = c_void_p
    PdfixLib.PdfixCreateDigSig.argtypes = [c_void_p]
    PdfixLib.PdfixCreateCustomDigSig.restype = c_void_p
    PdfixLib.PdfixCreateCustomDigSig.argtypes = [c_void_p]
    PdfixLib.PdfixCreateStandardSecurityHandler.restype = c_void_p
    PdfixLib.PdfixCreateStandardSecurityHandler.argtypes = [c_void_p, c_wchar_p, c_wchar_p, POINTER(zz_PdfStandardSecurityParams)]
    PdfixLib.PdfixCreateCustomSecurityHandler.restype = c_void_p
    PdfixLib.PdfixCreateCustomSecurityHandler.argtypes = [c_void_p, c_wchar_p, c_void_p]
    PdfixLib.PdfixRegisterSecurityHandler.restype = c_int
    PdfixLib.PdfixRegisterSecurityHandler.argtypes = [c_void_p, c_int, c_wchar_p, c_void_p]
    PdfixLib.PdfixRegisterAnnotHandler.restype = c_void_p
    PdfixLib.PdfixRegisterAnnotHandler.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfixRegisterActionHandler.restype = c_void_p
    PdfixLib.PdfixRegisterActionHandler.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfixCreateRegex.restype = c_void_p
    PdfixLib.PdfixCreateRegex.argtypes = [c_void_p]
    PdfixLib.PdfixCreateFileStream.restype = c_void_p
    PdfixLib.PdfixCreateFileStream.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfixCreateMemStream.restype = c_void_p
    PdfixLib.PdfixCreateMemStream.argtypes = [c_void_p]
    PdfixLib.PdfixCreateCustomStream.restype = c_void_p
    PdfixLib.PdfixCreateCustomStream.argtypes = [c_void_p, c_int, c_void_p]
    PdfixLib.PdfixRegisterEvent.restype = c_int
    PdfixLib.PdfixRegisterEvent.argtypes = [c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdfixUnregisterEvent.restype = c_int
    PdfixLib.PdfixUnregisterEvent.argtypes = [c_void_p, c_int, c_int, c_void_p]
    PdfixLib.PdfixReadImageInfo.restype = c_int
    PdfixLib.PdfixReadImageInfo.argtypes = [c_void_p, c_void_p, c_int, POINTER(zz_PsImageInfo)]
    PdfixLib.PdfixCreateImage.restype = c_void_p
    PdfixLib.PdfixCreateImage.argtypes = [c_void_p, c_int, c_int, c_int]
    PdfixLib.PdfixCreateRenderDeviceContext.restype = c_void_p
    PdfixLib.PdfixCreateRenderDeviceContext.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdfixRegisterPlugin.restype = c_int
    PdfixLib.PdfixRegisterPlugin.argtypes = [c_void_p, c_void_p, c_wchar_p]
    PdfixLib.PdfixGetPluginByName.restype = c_void_p
    PdfixLib.PdfixGetPluginByName.argtypes = [c_void_p, c_wchar_p]
    PdfixLib.PdfixGetEvent.restype = c_void_p
    PdfixLib.PdfixGetEvent.argtypes = [c_void_p]
    PdfixLib.PdfixFindSysFont.restype = c_void_p
    PdfixLib.PdfixFindSysFont.argtypes = [c_void_p, c_wchar_p, c_int, c_int]
    PdfixLib.PdfixLoadSettingsFromStream.restype = c_int
    PdfixLib.PdfixLoadSettingsFromStream.argtypes = [c_void_p, c_void_p, c_int]
    PdfixLib.PdfixGetTags.restype = c_int
    PdfixLib.PdfixGetTags.argtypes = [c_void_p, c_int, c_wchar_p, c_int]
    PdfixLib.PdfixGetSysFonts.restype = c_int
    PdfixLib.PdfixGetSysFonts.argtypes = [c_void_p, c_wchar_p, c_int]
    PdfixLib.PdfixGetRtlText.restype = c_int
    PdfixLib.PdfixGetRtlText.argtypes = [c_void_p, c_wchar_p, c_wchar_p, c_int]
    PdfixLib.PdfixPluginDestroy.restype = c_int
    PdfixLib.PdfixPluginDestroy.argtypes = [c_void_p]
    PdfixLib.PdfixPluginInitialize.restype = c_int
    PdfixLib.PdfixPluginInitialize.argtypes = [c_void_p, c_void_p]
    PdfixLib.PdfixPluginGetVersionMajor.restype = c_int
    PdfixLib.PdfixPluginGetVersionMajor.argtypes = [c_void_p]
    PdfixLib.PdfixPluginGetVersionMinor.restype = c_int
    PdfixLib.PdfixPluginGetVersionMinor.argtypes = [c_void_p]
    PdfixLib.PdfixPluginGetVersionPatch.restype = c_int
    PdfixLib.PdfixPluginGetVersionPatch.argtypes = [c_void_p]
    PdfixLib.PdfixPluginGetPdfixVersionMajor.restype = c_int
    PdfixLib.PdfixPluginGetPdfixVersionMajor.argtypes = [c_void_p]
    PdfixLib.PdfixPluginGetPdfixVersionMinor.restype = c_int
    PdfixLib.PdfixPluginGetPdfixVersionMinor.argtypes = [c_void_p]
    PdfixLib.PdfixPluginGetPdfixVersionPatch.restype = c_int
    PdfixLib.PdfixPluginGetPdfixVersionPatch.argtypes = [c_void_p]
    PdfixLib.PdfixPluginGetPdfix.restype = c_void_p
    PdfixLib.PdfixPluginGetPdfix.argtypes = [c_void_p]
    PdfixLib.GetPdfix.restype = c_void_p

def Pdfix_destroy():
    global PdfixLib
    del PdfixLib
    PdfixLib = None

