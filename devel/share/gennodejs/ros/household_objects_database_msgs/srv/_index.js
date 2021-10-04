
"use strict";

let GetModelList = require('./GetModelList.js')
let GetModelMesh = require('./GetModelMesh.js')
let GetModelScans = require('./GetModelScans.js')
let SaveScan = require('./SaveScan.js')
let GetModelDescription = require('./GetModelDescription.js')
let TranslateRecognitionId = require('./TranslateRecognitionId.js')

module.exports = {
  GetModelList: GetModelList,
  GetModelMesh: GetModelMesh,
  GetModelScans: GetModelScans,
  SaveScan: SaveScan,
  GetModelDescription: GetModelDescription,
  TranslateRecognitionId: TranslateRecognitionId,
};
